# Hello World App for Odoo

A simple Hello World application for Odoo that demonstrates basic functionality and serves as a great starting point for learning Odoo development.

## Features

- **Simple Model**: Create and manage hello world messages with different greeting types
- **User-Friendly Interface**: Clean form and tree views for easy interaction
- **Multiple Greeting Types**: Choose from Hello, Hi, Greetings, or Welcome
- **Active/Inactive Toggle**: Manage message visibility
- **Demo Data**: Comes with sample data for testing
- **Search & Filter**: Built-in search and filtering capabilities

## Compatibility

This app is compatible with:
- Odoo 16.0
- Odoo 17.0
- Odoo 18.0

## Installation

1. Copy the app folder to your Odoo addons directory
2. Update the apps list in Odoo
3. Install the "Hello World App" from the Apps menu

## Usage

1. Navigate to the "Hello World App" menu
2. Click "Create" to add a new message
3. Enter your name and select a greeting type
4. The personalized message will be automatically generated
5. Use the toggle button to activate/deactivate messages

## File Structure

```
hello_world_app/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── hello_world.py
├── views/
│   └── hello_world_views.xml
├── security/
│   └── ir.model.access.csv
├── data/
│   └── demo_data.xml
├── static/
│   └── description/
└── README.md
```

## Model Fields

- **Name**: The person's name (required)
- **Greeting Type**: Selection of greeting styles
- **Message**: Auto-generated personalized message
- **Active**: Toggle for message visibility
- **Created Date**: Timestamp of record creation

## Security

The app includes proper access rights for:
- Regular users (read, write, create, unlink)
- System administrators (full access)

## Demo Data

The app includes 5 sample records with different greeting types and active states for testing purposes.

## License

This app is licensed under LGPL-3.

## Support

For issues or questions, please contact the app developer.