"""The module defines the ContactList class."""

__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Signal

class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""

    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()
        self.__initialize_widgets()

        #connect __on_add_contact @Slot()
        self.add_button.clicked.connect(self.__on_add_contact)

        #connect __on_remove_contact @Slot()
        self.remove_button.clicked.connect(self.___on_remove_contact)

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    @Slot()
    def __on_add_contact(self) -> None:
        """
        on_add_contact (None): method will be a slot for the signal that occurs
        when the user clicks the Add Contact Button.

        dunder: naming convention makes on_add_contact private.

        status_label: String message notifying use to enter valid entries.
        """

        name = self.contact_name_input.text().strip()

        phone = self.phone_input.text().strip()

        if name and phone:
           row_position = self.contact_table.rowCount()
           self.contact_table.insertRow(row_position)

           name_item = QTableWidgetItem(name)
           phone_item = QTableWidgetItem(phone)

           self.contact_table.setItem(row_position, 0, name_item)
           self.contact_table.setItem(row_position, 1, phone_item)

           self.status_label.setText(f"Added contact: {name}")

        else:
            self.status_label.setText(
                "Plese enter a contact name and phone number")
        

    @Slot()
    def ___on_remove_contact(self) -> None:
        """
        on_remove_contact (None): method will be a slot for the signal that occurs
        when the user clicks the Remove Contact Button.

        dunder: naming convention makes on_remove_contact private.

        status_label: String message notifying user to select a row to remove
        """

        row = self.contact_table.currentRow()

        if row >= 0:

            reply = QMessageBox.question(self, "Remove Contact",
                "Are you sure you want to remove selected contact?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )

            if reply == QMessageBox.Yes:
                self.contact_table.removeRow(row)
                self.status_label.setText("Contact removed.")
            
        else:
            self.status_label.setText("Please select a row to be removed.")