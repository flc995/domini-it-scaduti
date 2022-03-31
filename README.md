<img src="https://raw.githubusercontent.com/flc995/domini-it-scaduti/main/static/intro.gif" alt="How-it-works" width="555px" />

# Tool di ricerca domini .it scaduti 🕚⚡️
[![GitHub issues](https://img.shields.io/github/issues/flc995/domini-it-scaduti)](https://github.com/flc995/domini-it-scaduti/issues)
[![GitHub forks](https://img.shields.io/github/forks/flc995/domini-it-scaduti)](https://github.com/flc995/domini-it-scaduti/network)
[![GitHub Repo stars](https://img.shields.io/github/stars/flc995/domini-it-scaduti)](https://github.com/flc995/domini-it-scaduti/stargazers)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/flc995/domini-it-scaduti)](https://github.com/flc995/domini-it-scaduti/releases)
[![GitHub last commit](https://img.shields.io/github/last-commit/flc995/domini-it-scaduti)](https://github.com/flc995/domini-it-scaduti/commits/main)

Un semplice script Python per ottenere la lista degli ultimi domini scaduti (massimo ultimi 8 giorni).\
I domini scaduti vengono scaricati dall'anagrafe dei domini italiani (nic.it) attraverso i file messi a disposizione dall'anagrafe stessa
al seguente indirizzo: https://www.nic.it/it/droptime

## Eseguire lo script
Per eseguire lo script occorre avere almeno Python 3.10
Installare le dipendenze eseguendo:
```
poetry install
```

È possibile eseguire lo script in modalita interattiva, e quindi verrano chiesti giorni e lunghezza del dominio come input.
```
poetry run search
```

Altrimenti è possibile eseguire lo script passando i requisiti come arguments:
```
poetry run search <int: days> <int: length> 
```

Esempio:
```
poetry run search 3 5
```

## Infrastruttura

- [Python](https://www.python.org/)


## Contributors Wall
<a href="https://github.com/flc995/domini-it-scaduti/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=flc995/domini-it-scaduti" />
</a>
