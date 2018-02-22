import click

@click.command()
@click.help_option('h', '--help')
@click.option('--name', prompt="Your name")
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))

def cli(name, input, output):
    print("this does nothing %s" % name)
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(chunk)


if __name__ == '__main__':
    cli()


#http://click.pocoo.org/5/arguments/
#https://www.novell.com/coolsolutions/feature/1652.html
#https://lifehacker.com/5272169/fast-is-a-geeky-command-line-database
