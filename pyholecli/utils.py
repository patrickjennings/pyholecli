def prep_arguments(arguments):
    arguments = [
        prep_arguments(argument) if isinstance(argument, list)
        else argument
        for argument in arguments
    ]
    return ' '.join(arguments)


def run_command(c, *args, **kwargs):
    command = prep_arguments(args)
    return c.run(command, **kwargs)


def put_file(c, local, remote, *args, **kwargs):
    return c.put(local, remote, *args, **kwargs)
