def adjust_tool_buttons(self=None):
    # Кнопка перехода на виджет настройки рабочего пространства
    self.toolButton_card.clicked.connect(self.toolButton_page_cardClick)

    self.toolButton_top_up.clicked.connect(self.toolButton_page_top_up_Click)

    self.toolButton_transaction.clicked.connect(self.toolButton_page_2_transactionClick)

def start_page_tool_buttos(self=None):
    self.toolButton_to_reg.clicked.connect(self.toolButton_to_regClick)
    self.toolButton_to_enter.clicked.connect(self.toolButton_to_enterClick)