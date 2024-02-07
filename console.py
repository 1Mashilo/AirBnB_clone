import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # Custom prompt

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_help(self, args):
        """Show help for available commands."""
        super().do_help(args)

    def do_emptyline(self, inp):
        """Handle empty line input (skip)."""
        pass  # Do nothing

if __name__ == '__main__':
    HBNBCommand().cmdloop()
