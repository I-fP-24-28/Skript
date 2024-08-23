```{=mermaid}
flowchart TD
    A(Start) --> B{venv}
    B --> | ja | C[activate venv]
    C --> D[code]
    D --> E[save work]
    E --> D
    E --> F[deactivate venv]
    F --> G(End)
    H[create venv]
    B --> | nein | H
    H --> C
```