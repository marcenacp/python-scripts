import click


@click.command()
@click.option('--argument1', default=1, help='first')
@click.option('--argument2', default=2, help='second')
def main(argument1, argument2):
    pass


if __name__ == '__main__':
    main()
    print('Done')
