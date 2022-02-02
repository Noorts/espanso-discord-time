<h1 align="center">
  <br>
  Espanso Discord Time
  <br>
</h1>
<h4 align="center">
  An Espanso trigger for Discord its local time feature
</h4>
<p align="center">
  <a href="#info">Info</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#license">License</a>
</p>

## Info
This repo contains a trigger for the text expander [Espanso](https://espanso.org/) that eases the use of Discord its local time feature. Discord allows you to write a unix timestamp as → `<t:1643787562>` which will turn into the reader its local time equivelant (for me in CET `February 2, 2022 8:39 AM`). This can be useful to quickly share times and dates without the need for the readers to convert the time into their local timezone.

## Installation
* [For Linux] Install Modulo manually to enable the use of forms with Espanso. See the forms [prerequisites](https://espanso.org/docs/forms/#prerequisites) page.
* Run `espanso edit` in your terminal to configure your espanso matches.
* Add the following trigger to the matches in your espanso config:
``` yaml
# Discord Local Time
  - trigger: "`dlt"
    replace: "<t:{{unixTimestamp}}> (← your local time)"
    vars:
      - name: mytime
        type: date
        params:
          format: "%a %d/%m/%Y - %H:%M"
      - name: form1
        type: form
        params:
          layout: |
            --- Your local time: ---
            {{name}}
          fields:
            name:
              default: "31-12-2022 23:59"
      - name: unixTimestamp
        type: script
        params:
          args:
            - python
            - "%CONFIG%/scripts/local_datetime_to_unix.py"
            - "$ESPANSO_FORM1_NAME"
```
* Run `espanso restart` if the config wasn't reloaded automatically.
* Navigate to your espanso config directory (`espanso path`) and add a `scripts` directory.
* Add the [local_datetime_to_unix.py](local_datetime_to_unix.py) script to your scripts directory.
* Ready to use!

## Usage
* Activate espanso by typing in the trigger `` `dlt ``.
* A form will pop up. Provide it a date and time in the provided default format.
(Note: This is in D-M-YYYY format. Adjust the trigger and Python script if you want it in a different format).
* Press <kbd>enter</kbd> (or <kbd>Ctrl+Enter</kbd> on MacOS).
* The correct Discord timestamp string should now appear.

## Alternatives
* Get the unix timestamp manually (with a [tool](https://www.unixtimestamp.com/) for example) and then write out your message.
* For iOS use one of the following shortcuts [#1](https://routinehub.co/shortcut/10154/) and [#2](https://www.peerreviewed.io/blog/2021/8/18/a-shortcut-for-generating-local-timestamps-in-discord).

## License
This repo is licensed under [The Unlicense](LICENSE).
