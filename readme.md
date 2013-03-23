# Example Overflow Sublime Text 2 Plugin

Example Overflow plugin searches and suggests code snippets based on Stack Overflow.

## How It Works
The plugin will use your query and your current syntax to search Stack Overflow. It will choose the top accepted answers, extract code snippets from them, and let you to choose one of them (from Sublime Text 2). 

This plugin uses the [SE API package](https://github.com/stared/se-api-py) 

## Install
The suggested method is to use the [Sublime Package Manager](http://wbond.net/sublime_packages/package_control).

## Use
Use one of the following key bindings

- 'Ctrl + o' : to use the selected text (or code) as the search query
- 'Shift + Ctrl + o' : to open a search input panel at the bottom
- use 'Super' instead of 'Ctrl' for OS X

The plugin will open a quick panel with the top results (title and tags from StackOverflow). Upon choosing one of the results a new buffer will open with a pasted code snippet. 

Alternatively it is possible to use the Command Palette (Ctrl+Shift+P) instead of the key bindings.

## Beta
This plugin is in early development and may not work properly (or at all). Its design is still under development (I'm open to suggestions).

---
Copyright (C) 2013 Alexey Zagalsky

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.