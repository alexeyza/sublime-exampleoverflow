import sublime
import sublime_plugin
import SEAPI
import re


def search_for(self, query):
    so = SEAPI.SEAPI(site="stackoverflow")
    search_results = so.fetch_one("search/advanced", q=query, order='desc', sort='relevance', accepted='true', filter='default')
    ids = [q['accepted_answer_id'] for q in search_results]
    answers = so.fetch_one("answers/{ids}", ids=ids, filter='!-.mgWLrmFjzN')
    data = [(answer['title'], answer['tags'], answer['body'], answer['question_id']) for answer in answers]
    return data


def create_results(self, data):
    results = []
    for item in data:
        single_res = []
        single_res.append(item[0])
        single_res.append(u','.join(item[1]))
        results.append(single_res)
    return results


def get_comment_line_character(syntax):
    return {
        'Java': '//',
        'Python': '##',
        'JavaScript': '//',
    }.get(syntax, '//')


class ExampleoverflowSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)
            text = self.view.substr(selection)
            # find the user's syntax highlighting language
            syntax = self.view.settings().get('syntax')
            self.original_syntax = syntax
            match = re.search(r'Packages/[\w\s]+/([\w\s]+)[.]+tmLanguage', syntax)
            if not match is None:
                syntax = match.group(1)

            # call for search and store results in so_results
            self.so_results = search_for(self, syntax+' '+text)

            # create a new array with results to fit the quick panel
            messages = create_results(self, self.so_results)

            # open quick panel and show results
            self.show_quick_panel(messages, self.view.window())

    Results = ''

    def print_output(self, output):
        if not self.Results:  # or not self.Results in view.window().views():
            # Need to create Results scratch buffer
            self.Results = self.view.window().new_file()
            self.Results.set_scratch(True)
            self.Results.set_name("Search Results")

        edit = self.Results.begin_edit('insert')
        self.Results.insert(edit, 0, output)
        self.Results.end_edit(edit)
        self.Results.set_syntax_file(self.original_syntax)

    def on_done(self, picked):
        if picked == -1:
            return
        question_id = self.so_results[picked][3]
        match = re.findall(ur'<pre><code>(.+?)</code></pre>', self.so_results[picked][2], re.DOTALL)
        code_snippet = ''
        comment_char = get_comment_line_character(self.original_syntax)
        question_url = comment_char+' The following code snippet was taken from:\n'+comment_char+' http://stackoverflow.com/questions/'+str(question_id)+'\n\n'
        code_snippet = question_url+' '.join(match)
        self.print_output(code_snippet)

    def show_quick_panel(self, messages, window):
        window.show_quick_panel(messages, self.on_done, sublime.MONOSPACE_FONT)


class ExampleoverflowSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search for', '', self.on_input_done, self.on_change, self.on_cancel)

    def on_input_done(self, input):
        # find the user's syntax highlighting language
        syntax = self.window.active_view().settings().get('syntax')
        self.original_syntax = syntax
        match = re.search(r'Packages/[\w\s]+/([\w\s]+)[.]+tmLanguage', syntax)
        if not match is None:
            syntax = match.group(1)

        # call for search and store results in so_results
        self.so_results = search_for(self, syntax+' '+input)

        # create a new array with results to fit the quick panel
        messages = create_results(self, self.so_results)

        # open quick panel and show results
        self.show_quick_panel(messages, self.window)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

    Results = ''

    def print_output(self, output):
        if not self.Results:  # or not self.Results in view.window().views():
            # Need to create Results scratch buffer
            self.Results = self.window.new_file()
            self.Results.set_scratch(True)
            self.Results.set_name("Search Results")

        edit = self.Results.begin_edit('insert')
        self.Results.insert(edit, 0, output)
        self.Results.end_edit(edit)
        self.Results.set_syntax_file(self.original_syntax)

    def on_done(self, picked):
        if picked == -1:
            return
        question_id = self.so_results[picked][3]
        match = re.findall(ur'<pre><code>(.+?)</code></pre>', self.so_results[picked][2], re.DOTALL)
        code_snippet = ''
        comment_char = get_comment_line_character(self.original_syntax)
        question_url = comment_char+' The following code snippet was taken from:\n'+comment_char+' http://stackoverflow.com/questions/'+str(question_id)+'\n\n'
        code_snippet = question_url+' '.join(match)
        self.print_output(code_snippet)

    def show_quick_panel(self, messages, window):
        window.show_quick_panel(messages, self.on_done, sublime.MONOSPACE_FONT)
