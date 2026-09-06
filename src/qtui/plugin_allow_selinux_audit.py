# Copyright (C) 2022-2026 The MIO-KITCHEN-SOURCE Project
#
# Licensed under the GNU AFFERO GENERAL PUBLIC LICENSE, Version 3.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.gnu.org/licenses/agpl-3.0.en.html#license-text
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from PySide6.QtWidgets import QHBoxLayout, QFileDialog
from qfluentwidgets import (
    LineEdit, BodyLabel, PushButton, MessageBoxBase
)


class AllowSELinuxAuditMessageBox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. Dialog Header Title
        self.titleLabel = BodyLabel(self.tr("Allow SELinux audit"), self)
        self.titleLabel.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.setSpacing(16)

        # 2. Row 1: Log file selection
        log_layout = QHBoxLayout()
        log_layout.setSpacing(10)

        self.log_label = BodyLabel(self.tr("Log file:"))
        self.log_label.setFixedWidth(100)

        self.log_path_edit = LineEdit()

        self.choose_log_btn = PushButton(self.tr("Choose"))
        self.choose_log_btn.setFixedWidth(85)
        self.choose_log_btn.clicked.connect(self.open_file_dialog)

        log_layout.addWidget(self.log_label)
        log_layout.addWidget(self.log_path_edit, 1)
        log_layout.addWidget(self.choose_log_btn)
        self.viewLayout.addLayout(log_layout)

        # 3. Row 2: Output folder selection
        output_layout = QHBoxLayout()
        output_layout.setSpacing(10)

        self.output_label = BodyLabel(self.tr("Output folder:"))
        self.output_label.setFixedWidth(100)

        self.output_path_edit = LineEdit()

        self.choose_output_btn = PushButton(self.tr("Choose"))
        self.choose_output_btn.setFixedWidth(85)
        self.choose_output_btn.clicked.connect(self.open_folder_dialog)

        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_path_edit, 1)
        output_layout.addWidget(self.choose_output_btn)
        self.viewLayout.addLayout(output_layout)

        # 4. Action Buttons Configuration
        self.yesButton.setText(self.tr("Run"))
        self.cancelButton.setText(self.tr("Close"))



        # Set clean dimensions matching the screenshot layout aspect ratio
        self.widget.setMinimumWidth(480)

    def open_file_dialog(self):
        """Opens native file picker to target the audit log file."""
        file_path, _ = QFileDialog.getOpenFileName(
            self, self.tr("Select SELinux Log File"), "", "Log Files (*.log *.txt);;All Files (*)"
        )
        if file_path:
            self.log_path_edit.setText(file_path)

    def open_folder_dialog(self):
        """Opens native directory picker to target the output folder."""
        folder_path = QFileDialog.getExistingDirectory(self, self.tr("Select Output Directory"), "")
        if folder_path:
            self.output_path_edit.setText(folder_path)

