# Python CLI To-Do List

A simple command line To-Do list application built with Python.

## Features

- Add tasks
- View tasks
- Edit tasks
- Remove tasks
- Mark tasks as completed
- Save tasks automatically using JSON

## How it works

Tasks are stored in a JSON file (`tarefas.json`) so they persist even after closing the program.

Each task has the structure:

```json
{
  "texto": "Study Python",
  "concluida": false
}
