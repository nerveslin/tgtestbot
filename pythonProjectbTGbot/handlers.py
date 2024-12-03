from aiogram import F, Bot, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboards as kb

from config import TOKEN

from tgdatabase import add_task, complete_task, delete_task, list_tasks

bot = Bot(TOKEN)
router = Router()


class RegisterTask(StatesGroup):
    # task_name = State()
    task_menu = State("task_menu")
    delete_menu = State("delete_menu")
    list_menu = State("list_menu")


@router.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    await message.answer(f'Welcome, {message.from_user.first_name}!\nYour ID is {message.from_user.id}.'
                         f'Choose what to do:',
                         reply_markup=kb.main)
    await state.set_state(RegisterTask.task_menu)


# @router.callback_query(F.data == 'add_task')
# async def add_task_to_list(callback: types.CallbackQuery, state: FSMContext):
#     await callback.answer('Noted')
#     await callback.message.answer('Enter the task name')
#     await state.set_state(RegisterTask.task_name)
#
#
# @router.message(RegisterTask.task_name)
# async def add_task_name(message: types.Message, state: FSMContext):
#     task_name = message.text
#     await add_task(task_name)
#     await message.answer(f'Task {task_name} has been set successfully.',
#                          reply_markup=kb.main)


@router.callback_query(lambda c: c.data == "add_task")
async def add_task_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the task name:")
    await state.set_state(RegisterTask.task_menu)


@router.callback_query(lambda c: c.data == "delete_task")
async def delete_task_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the task ID to delete:")
    await state.set_state(RegisterTask.delete_menu)


@router.callback_query(lambda c: c.data == "complete_task")
async def complete_task_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Enter the task ID to mark as completed:")
    await state.set_state(RegisterTask.list_menu)


@router.callback_query(lambda c: c.data == "list_tasks")
async def list_tasks_handler(callback_query: types.CallbackQuery):
    tasks = list_tasks()
    await callback_query.message.answer("Tasks in the database:")
    if not tasks:
        await callback_query.message.answer("No tasks found")
        return
    for task in tasks:
        task_id, task_name, completed, time = task
        status = "Yes" if completed else "No"
        response = f"ID: {task_id}, Name: {task_name}, Completed: {status}, Time: {time}"
        await callback_query.message.answer(response)
    await callback_query.message.answer("No more tasks in the database")


@router.message(RegisterTask.task_menu)
async def task_name_handler(message: types.Message, state: FSMContext):
    task_name = message.text
    add_task(task_name)
    await message.answer(f"Task '{task_name}' added successfully!")
    await state.clear()


@router.message(RegisterTask.delete_menu)
async def delete_task_handler(message: types.Message, state: FSMContext):
    try:
        task_id = int(message.text)
        delete_task(task_id)
        await message.answer(f"Task with ID {task_id} deleted successfully!")
    except ValueError:
        await message.answer("Please enter a valid task ID.")
    await state.clear()


@router.message(RegisterTask.list_menu)
async def complete_task_handler(message: types.Message, state: FSMContext):
    try:
        task_id = int(message.text)
        complete_task(task_id)
        await message.answer(f"Task with ID {task_id} marked as completed!")
    except ValueError:
        await message.answer("Please enter a valid task ID.")
    await state.clear()


# @router.message(RegisterTask.task_menu)
# async def task_menu_handler(message: types.Message, state: FSMContext):
#     if message.text == "Add task":
#         await message.answer("Enter the task name.")
#         task_name = message.text
#         await add_task(task_name)
#     elif message.text == "Delete task":
#         await message.answer("Choose an option:",
#                              reply_markup=kb.delete_task)
#         await state.set_state(RegisterTask.delete_menu)
#     elif message.text == "Mark task as completed":
#         await message.answer("Enter task ID.")
#         task_id = int(message.text)
#         complete_task(task_id)
#     elif message.text == "List tasks":
#         await message.answer("Choose an option",
#                              reply_markup=kb.list_task)
#         await state.set_state(RegisterTask.list_menu)
#
#
# @router.message(RegisterTask.delete_menu)
# async def delete_menu_handler(message: types.Message, state: FSMContext):
#     if message.text == "Delete task by ID":
#         await message.answer("Enter task ID.")
#         task_id = int(message.text)
#         await delete_task(task_id)
#     elif message.text == "Delete all tasks":
#         await delete_all()
#     elif message.text == "Return to main menu":
#         await message.answer(f'Returning to main menu. Choose what to do:',
#                              reply_markup=kb.main)
#         await state.set_state(RegisterTask.task_menu)
#
#
# @router.message(RegisterTask.list_menu)
# async def list_menu_handler(message: types.Message, state: FSMContext):
#     if message.text == "List task by ID":
#         await message.answer("Enter task ID")
#         task_id = int(message.text)
#         await get_task(task_id)
#     elif message.text == "List all tasks":
#         await list_tasks()
#     elif message.text == "Return to main menu":
#         await message.answer(f'Returning to main menu. Choose what to do',
#                              reply_markup=kb.main)
#         await state.set_state(RegisterTask.task_menu)


# @router.message(Command('register'))
# async def register(message: Message, state: FSMContext):
#     await state.set_state(Register.role)
#     await message.answer('Enter your role')
#
#
# @router.message(Register.role)
# async def register_role(message: Message, state: FSMContext):
#     await state.update_data(role=message.text)
#     await state.set_state(Register.age)
#     await message.answer('Enter your age')
#
#
# @router.message(Register.age)
# async def register_age(message: Message, state: FSMContext):
#     await state.update_data(age=message.text)
#     await state.set_state(Register.number)
#     await message.answer('Enter your number', reply_markup=kb.get_number)
#
#
# @router.message(Register.number, F.contact)
# async def register_number(message: Message, state: FSMContext):
#     await state.update_data(number=message.contact.phone_number)
#     data = await state.get_data()
#     await message.answer(f'Your role: {data["role"]}\nYour age: {data["age"]}\nYour phone number: {data["number"]}')
#     await state.clear()
#
#
# @router.message(F.text == 'Task 1')
# async def taskmanager(message: Message):
#     await message.answer('Choose the most important task', reply_markup=kb.taskmanager)
#
#
# @router.callback_query(F.data == 'all_tasks')
# async def essay(callback: CallbackQuery):
#     await callback.answer('Noted')
#     await callback.message.answer('This should pull up all tasks')
