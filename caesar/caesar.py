import unicodedata
import click

def c_cipher(text, shift, file): 
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").upper()
    c_text = ""
    for char in text:
        if char >= "A" and char <= "Z":
            position = ord(char) - 65
            new_position = (position + shift) % 26
            c_text += chr(new_position + 65)
        elif char == " ":
            c_text += chr(45) # chr(45) => -
    if file:
        with open(file, "w") as f:
            f.write(c_text)
    else:
        click.echo("No file :(")

@click.command()
@click.argument("text", required=False, default=None)
@click.option("-sh", "--shift", default=3, help="How many positions you want to shift your cipher!")
@click.option("-f", "--file", default="default.txt", help="Place where you save it!")
@click.option("-d", "--description", is_flag=True, help="No argument, just write: '--description' to decode")

def main(text, shift, file, description):
    if text is None:
        text = input("text not defined\nWrite it now > ")
    if description:
        shift = -shift
    c_cipher(text, shift, file)

if __name__ == "__main__":
    main()
