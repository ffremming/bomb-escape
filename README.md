# Bomb Escape

Et rutenett-basert overlevelsesspill i terminalen — løp fra fienden, samle mynter og bryt gjennom hindringer med granater og bomber. Skrevet i Python.

![Skjermbilde](screenshot.png)

## Om prosjektet

Skrevet i 1. klasse på informatikk ved Universitetet i Oslo som en oppfølger til [Terminal Pokémon](https://github.com/ffremming/terminal-pokemon). Jeg ønsket å eksperimentere mer med kobling mellom celler (naboliste), en enkel fiende-AI som jakter på spilleren, og rekursive eksplosjoner.

## Hva den gjør

- Et rutenett med spiller, fiende, mynter og hindringer (genereres tilfeldig rundt "ankere")
- Fienden beveger seg mot spilleren — spillet er over hvis den når deg
- Samle mynter for poeng
- Bruk granater (`g`) for å sprenge en celle i retning du beveger deg, eller en bombe (`b`) for å sprenge cellene rundt deg
- Kommandoer: `o`/`n`/`h`/`v` for retning, `g` for granat, `b` for bombe, enter for å bevege

## Kjøring

```bash
python brett.py
```

Ingen eksterne avhengigheter — bare standard Python 3.
