import sys
from PyQt5.QtWidgets import *
import requests
import json
from qt_material import apply_stylesheet
class Demo(QWidget):
    language_list = ['中文', '英语', '日语', '韩语', '法语']
    prefix='http://translate.google.cn/translate_a/single?client=gtx&dt=t&dj=1&ie=UTF-8'
    def __init__(self):
        super(Demo, self).__init__()
        self.edit_label = QLabel('原文', self)
        self.browser_label = QLabel('译文', self)
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)
        self.trans_button = QPushButton('翻译',self)
        self.src_combobox = QComboBox(self)
        self.dst_combobox = QComboBox(self)
        self.src_combobox.addItem('自动检测')
        self.src_combobox.addItems(self.language_list)
        self.dst_combobox.addItems(self.language_list)
        self.dic = {
            '自动检测': 'auto',
            '中文': 'zh_CN',
            '英语': 'en',
            '日语': 'ja',
            '韩语': 'ko',
            '法语': 'fr'
        }

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.all_layout = QVBoxLayout()
        
        
        self.layout_init()
        self.trans_button.clicked.connect(self.translate)

    def translate(self):
        keys = {
            'sl': self.dic[self.src_combobox.currentText()],
            'tl': self.dic[self.dst_combobox.currentText()],
            'q': self.text_edit.toPlainText()
        }
        res = requests.get(self.prefix, params=keys)
        res.encoding = 'utf-8'
        data=json.loads(res.text)
        self.text_browser.setText(data['sentences'][0]['trans'])

    def layout_init(self):
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.src_combobox)
        self.edit_v_layout.addWidget(self.text_edit)
        self.browser_v_layout.addWidget(self.browser_label)
        self.browser_v_layout.addWidget(self.dst_combobox)
        self.browser_v_layout.addWidget(self.text_browser)

        self.top_layout.addLayout(self.edit_v_layout)
        self.top_layout.addLayout(self.browser_v_layout)

        self.all_layout.addLayout(self.top_layout)
        self.all_layout.addWidget(self.trans_button)

        self.setLayout(self.all_layout)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = Demo()
    apply_stylesheet(app, theme='dark_teal.xml')
    demo.show()
    sys.exit(app.exec())    