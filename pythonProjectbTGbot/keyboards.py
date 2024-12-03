from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Add task', callback_data='add_task')],
    [InlineKeyboardButton(text='Delete task', callback_data='delete_task')],
    [InlineKeyboardButton(text='Mark task as completed', callback_data='complete_task')],
    [InlineKeyboardButton(text='List tasks', callback_data='list_tasks')]])

delete_task = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Delete task by ID', callback_data='delete_id')],
    [InlineKeyboardButton(text='Delete all tasks', callback_data='delete_all')],
    [InlineKeyboardButton(text='Return to main menu', callback_data='return')]])

# list_task = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='List task by ID', callback_data='list_id')],
#     [InlineKeyboardButton(text='List all tasks', callback_data='list_all')],
#     [InlineKeyboardButton(text='Return to main menu', callback_data='return')]],
#                                 resize_keyboard=True,
#                                 input_field_placeholder='Choose an option')

taskmanager = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Check tasks', callback_data='all_tasks')],
    [InlineKeyboardButton(text='Add new task', callback_data='add_new')],
    [InlineKeyboardButton(text='Mark task as completed', callback_data='mark_task')]])

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Enter number automatically',
                                                           request_contact=True)]],
                                 resize_keyboard=True)