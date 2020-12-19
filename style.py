def btnStyle():
    return """
    QPushButton{
        background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 #08729A, stop: 1 white);
        border-style: outset;
        border-width: 2px;
        border-radius: 8px;
        border-color: #052D3D;
        font: 12px;
        padding: 2px;
        min-width: 2em;
    }
    """
def displayLabelStyle():
    return """
    QWidget {
            font: 13pt Times Bold;
            color: #052D3D;
            background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 #08729A, stop: 1 white);
                    }
            """
