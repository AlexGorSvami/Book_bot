import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu

#Инициализирую логгер
logger = logging.getLogger(__name__)

#Функция конфигурации и запуска бота
async def main():
    # Конфигурация логирования
    logging.basicConfig(level=logging.INFO,
                        format='%(filename)s:%(lineno)d #%(levelname)-8s '
                               '[%(asctime)s] - %(name)s - %(message)s)')

    #Вывожу в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    #Загружаю конфиг в переменную config
    config: Config = load_config()

    # Инициализирую бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token,
                   parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    #Настраиваю главное меню бота
    await set_main_menu(bot)

    #Регестрирую роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    #Пропускаю накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

