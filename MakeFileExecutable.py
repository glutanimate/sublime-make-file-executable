import sublime, sublime_plugin, os, subprocess
 
class MakeFileExecutable(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            file_name = self.view.file_name()
            subprocess.Popen(["chmod", "+x", file_name])
            sublime.status_message("Changed permissions for %s" % file_name)