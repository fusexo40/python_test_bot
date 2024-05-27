from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import keyboards as kb

router = Router()


pari = []


class Moves(StatesGroup):
    mainmenu = State()
    create = State()


@router.message(Command('start'))
async def main(message: Message, state: FSMContext):
    await main(message, state)


@router.message(Moves.mainmenu)
async def main(message: Message, state: FSMContext):
    await message.answer("Ку", reply_markup=kb.main_kb)


@router.message(F.text == "Мои пари")
async def pari_lst(message: Message):
    if pari:
        st = ""
        for i in pari:
            st += i + "\n"
        await message.answer(st)
    else:
        await message.answer("У вас нет пари")


@router.message(F.text == "Создать пари")
async def create_par(message: Message, state: FSMContext):
    await message.answer("Введите название пари", reply_markup=kb.create_kb)
    await state.set_state(Moves.create)


@router.message(Moves.create)
async def add_pari(message: Message, state: FSMContext):
    await message.answer("Пари успешно добавлено")
    pari.append(message.text)


@router.message(F.data == "main")
async def main_menu_state(callback_data: CallbackQuery, state: FSMContext):
    await callback_data.answer("Назад")
    await state.set_state(Moves.mainmenu)




