# IEEE Hackathon Website Template

A Discord bot created for use in hackathons run by [IEEE University of Toronto Student Branch](https://ieee.utoronto.ca/).

## IEEE Web Team 2022-2023
#### Directors
- YuYing Liang
- Leo Haocheng Li
- Mustafa Abdulrahman (PM)

#### Associates
- Ethan Hugh
- Luke Cheseldine
- Karandeep Lubana
- Terry Luan
- Eric Ji
- Dalia Mahidashti 
- Carmen Chau
- Samuel Liu
- Daniel Qiu

## Contents
- [Requirements](#requirements)
- [Getting Started](#getting-started)
    * [Installing Requirements](#installing-requirements)
    * [Environment Variables](#environment-variables)
    * [Adding the Bot to your server](#adding-the-bot-to-your-server)

## Requirements
- Python 3.8 or higher
- A Discord account

## Getting Started

To get started, go to the [Discord Developer Portal][https://discord.com/developers/applications]. Create a "New Application", and under the Bot tab, add a Bot. You can now get the API token under the "Token" Category. This is the `DISCORD_API_SECRET` environment variable you will be using.

### Installing Requirements
Install the requirements in `requirements.txt`. This should be done regularly as new requirements are added, not just the first time you set up.
```bash
$ pip install -r requirements.txt
```

### Environment Variables
For ease of use a [.env file][https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1] will be used. Below is a table of environment variables that will be used. Those in **bold** are required.
| **Variable**   | **Required value**                | **Default**       | **Description**                                                                   |
|:--------------:|:---------------------------------:|:-----------------:|:---------------------------------------------------------------------------------:|
| **DISCORD_API_SECRET**| API SECRET FROM DEV PORTAL |                   |  The API to connect your App with the Discord bot                                 |
| cmd_prefix     |                                   |         /         |  The prefix to prepend to a command, when a user attempts to use a command        |
| description    |                                   |                   |  A description of the Discord bot                                                 |



### Adding the Bot to your server
Navigate to the "OAuth2" -> "URL Generator" tab. Select the "bot" and "Administrator" options. Navigate to the Generated URL, and add the bot to any server

