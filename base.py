import click


@click.command()
@click.option('--argument', default=1, help='argument')
@click.option('--file', default='./file', type=click.File('rb'), help='file')
def main(argument, file):
    pass


if __name__ == '__main__':
    main()
    print('Done')
