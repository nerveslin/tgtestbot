from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Add task', callback_data='add_task')],
    [InlineKeyboardButton(text='Delete task', callback_data='delete_task')],
    [InlineKeyboardButton(text='Mark task as completed', callback_data='complete_task')],
    [InlineKeyboardButton(text='List tasks', callback_data='list_tasks')]])

delete_task = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Delete task by ID', callback_data='delete_id')],
    [InlineKeyboardButton(text='Delete all tasks', callback_data='delete_all')],
    [InlineKeyboardButton(text='Return to main menu', callback_data='return')]])
