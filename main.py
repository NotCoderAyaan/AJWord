import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import docx2txt


class AJWord(QMainWindow):
    def __init__(self):
        super(AJWord, self).__init__()
        self.editor = QTextEdit()
        self.editor.setFontPointSize(20)
        self.setCentralWidget(self.editor)
        self.font_size_box = QSpinBox()
        self.showMaximized()
        self.setWindowTitle('AJWord')
        self.create_toolbar()
        self.createmenubar()

    def createmenubar(self):
        menubar = QMenuBar()

        file_menu = QMenu('File', self)
        menubar.addMenu(file_menu)

        save_as_pdfaction = QAction('Save as PDF', self)
        save_as_pdfaction.triggered.connect(self.save_as_pdf)
        file_menu.addAction(save_as_pdfaction)

        edit_menu = QMenu('Edits', self)
        menubar.addMenu(edit_menu)

        view_menu = QMenu('Views', self)
        menubar.addMenu(view_menu)

        self.setMenuBar(menubar)

    def create_toolbar(self):
        tool_bar = QToolBar()
        self.addToolBar(tool_bar)

        undo = QAction(QIcon('undo.png'),'undo', self)
        undo.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo)

        redo = QAction(QIcon('redo.png'), 'redo', self)
        redo.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo)

        tool_bar.addSeparator()
        tool_bar.addSeparator()

        cut = QAction(QIcon('cut.png'), 'cut', self)
        cut.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut)

        copy = QAction(QIcon('copy.png'), 'copy', self)
        copy.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy)

        paste = QAction(QIcon('paste.png'), 'paste', self)
        paste.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste)

        tool_bar.addSeparator()
        tool_bar.addSeparator()

        italic_action = QAction(QIcon("italic.png"), 'Italic', self)
        italic_action.triggered.connect(self.italic_text)
        tool_bar.addAction(italic_action)

        bold_action = QAction(QIcon("bold.png"), 'Bold', self)
        bold_action.triggered.connect(self.bold_text)
        tool_bar.addAction(bold_action)

        tool_bar.addSeparator()
        tool_bar.addSeparator()

        right_alignment_action = QAction(QIcon("right-align.png"), 'Align Right', self)
        right_alignment_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignRight))
        tool_bar.addAction(right_alignment_action)

        left_alignment_action = QAction(QIcon("left-align.png"), 'Align Left', self)
        left_alignment_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignLeft))
        tool_bar.addAction(left_alignment_action)

        justification_action = QAction(QIcon("justification.png"), 'Center/Justify', self)
        justification_action.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignCenter))
        tool_bar.addAction(justification_action)

        self.font_size_box.setValue(20)
        self.font_size_box.valueChanged.connect(self.set_font_size)
        tool_bar.addWidget(self.font_size_box)
        self.addToolBar(tool_bar)

        tool_bar.addSeparator()
        tool_bar.addSeparator()



    def set_font_size(self):
        value = self.font_size_box.value()
        self.editor.setFontPointSize(value)

    def save_as_pdf(self):
        filepath, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF Files (*.pdf)')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(filepath)
        self.editor.document().print_(printer)

    def italic_text(self):
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not (state))

    def bold_text(self):
        if self.editor.fontWeight() != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)
            return
        self.editor.setFontWeight(QFont.Normal)

app = QApplication(sys.argv)
window = AJWord()
window.show()
sys.exit(app.exec_())
