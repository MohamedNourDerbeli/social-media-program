# Social Media Application using Tkinter and WebView

**Table of Contents**
- [Overview](#overview)
- [Features](#features)
- [Components](#components)
- [How to Use](#how-to-use)
- [Prerequisites](#prerequisites)
- [Development](#development)
- [Disclaimer](#disclaimer)

## Overview

This Python application creates a graphical user interface (GUI) for accessing popular social media platforms, including Facebook, Instagram, Twitter, and TikTok. It uses the Tkinter library for GUI development and WebView to embed web views within the application. Users can open each platform in a dedicated WebView window directly from the application.

## Features

- **Access Social Media:** You can access Facebook, Instagram, Twitter, and TikTok from a single window.

- **Dedicated Buttons:** The application provides dedicated buttons on the sidebar for each social media platform, making it easy to navigate.

- **Customizable WebView Windows:** Each WebView window can be customized in terms of width, height, background color, and position on the screen. They are also resizable and zoomable.

## Components

### GUI
- The main GUI is built with Tkinter and includes the following elements:
  - A top title with the application name.
  - A logo representing the application.
  - A brief text description of the application.
  - A sidebar with buttons for each social media platform.
  - A main application frame for displaying the WebView windows.

### WebView
- The WebView library is used to create and manage the web views for each social media platform. Each platform has a corresponding function (e.g., `Facebook()`, `Instagram()`) that creates a WebView window and loads the respective social media website.

## How to Use

1. Run the Python script.
2. The main application window will open, displaying the application name, logo, and a list of social media platforms in the sidebar.
3. Click on a platform button in the sidebar to open a WebView window for that platform.
4. You can interact with the social media platform just like you would in a regular web browser.

## Prerequisites

- Ensure that Python is installed on your system.
- If not already installed, use `pip install webview` to install the `webview` library.

## Development

- You can further customize the application by modifying the functions for each platform (e.g., adding more platforms or changing their appearance).

## Disclaimer

This application is intended for educational and personal use only. It is not affiliated with or endorsed by any of the social media platforms it provides access to. Use responsibly and adhere to the terms of service of the respective platforms.
