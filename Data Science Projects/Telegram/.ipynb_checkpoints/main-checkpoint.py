{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e1142afe-3f5c-4e1e-8520-398dd7027399",
   "metadata": {},
   "source": [
    "# Telegram Bot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bd60330a-abf8-4578-a42b-e42f0d05e827",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: python-telegram-bot in c:\\programdata\\anaconda3\\lib\\site-packages (21.3)\n",
      "Requirement already satisfied: httpx~=0.27 in c:\\users\\walter owando\\appdata\\roaming\\python\\python311\\site-packages (from python-telegram-bot) (0.27.0)\n",
      "Requirement already satisfied: anyio in c:\\programdata\\anaconda3\\lib\\site-packages (from httpx~=0.27->python-telegram-bot) (4.2.0)\n",
      "Requirement already satisfied: certifi in c:\\programdata\\anaconda3\\lib\\site-packages (from httpx~=0.27->python-telegram-bot) (2024.6.2)\n",
      "Requirement already satisfied: httpcore==1.* in c:\\users\\walter owando\\appdata\\roaming\\python\\python311\\site-packages (from httpx~=0.27->python-telegram-bot) (1.0.5)\n",
      "Requirement already satisfied: idna in c:\\programdata\\anaconda3\\lib\\site-packages (from httpx~=0.27->python-telegram-bot) (3.7)\n",
      "Requirement already satisfied: sniffio in c:\\programdata\\anaconda3\\lib\\site-packages (from httpx~=0.27->python-telegram-bot) (1.3.0)\n",
      "Requirement already satisfied: h11<0.15,>=0.13 in c:\\users\\walter owando\\appdata\\roaming\\python\\python311\\site-packages (from httpcore==1.*->httpx~=0.27->python-telegram-bot) (0.14.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install python-telegram-bot --upgrade"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5dc6343d-a9d0-4834-b411-3f48cf982ffc",
   "metadata": {},
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "Cannot close a running event loop",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\telegram\\ext\\_application.py:1069\u001b[0m, in \u001b[0;36mApplication.__run\u001b[1;34m(self, updater_coroutine, stop_signals, close_loop)\u001b[0m\n\u001b[0;32m   1068\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m-> 1069\u001b[0m     loop\u001b[38;5;241m.\u001b[39mrun_until_complete(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39minitialize())\n\u001b[0;32m   1070\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mpost_init:\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\asyncio\\base_events.py:629\u001b[0m, in \u001b[0;36mBaseEventLoop.run_until_complete\u001b[1;34m(self, future)\u001b[0m\n\u001b[0;32m    628\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_closed()\n\u001b[1;32m--> 629\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_running()\n\u001b[0;32m    631\u001b[0m new_task \u001b[38;5;241m=\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m futures\u001b[38;5;241m.\u001b[39misfuture(future)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\asyncio\\base_events.py:588\u001b[0m, in \u001b[0;36mBaseEventLoop._check_running\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    587\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_running():\n\u001b[1;32m--> 588\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mThis event loop is already running\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m    589\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[1;31mRuntimeError\u001b[0m: This event loop is already running",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\telegram\\ext\\_application.py:1094\u001b[0m, in \u001b[0;36mApplication.__run\u001b[1;34m(self, updater_coroutine, stop_signals, close_loop)\u001b[0m\n\u001b[0;32m   1093\u001b[0m         loop\u001b[38;5;241m.\u001b[39mrun_until_complete(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mpost_stop(\u001b[38;5;28mself\u001b[39m))\n\u001b[1;32m-> 1094\u001b[0m loop\u001b[38;5;241m.\u001b[39mrun_until_complete(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mshutdown())\n\u001b[0;32m   1095\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mpost_shutdown:\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\asyncio\\base_events.py:629\u001b[0m, in \u001b[0;36mBaseEventLoop.run_until_complete\u001b[1;34m(self, future)\u001b[0m\n\u001b[0;32m    628\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_closed()\n\u001b[1;32m--> 629\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_running()\n\u001b[0;32m    631\u001b[0m new_task \u001b[38;5;241m=\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m futures\u001b[38;5;241m.\u001b[39misfuture(future)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\asyncio\\base_events.py:588\u001b[0m, in \u001b[0;36mBaseEventLoop._check_running\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    587\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_running():\n\u001b[1;32m--> 588\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mThis event loop is already running\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m    589\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[1;31mRuntimeError\u001b[0m: This event loop is already running",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 43\u001b[0m\n\u001b[0;32m     40\u001b[0m app\u001b[38;5;241m.\u001b[39madd_handler(MessageHandler(filters\u001b[38;5;241m.\u001b[39mTEXT \u001b[38;5;241m&\u001b[39m \u001b[38;5;241m~\u001b[39mfilters\u001b[38;5;241m.\u001b[39mCOMMAND, unknown_text))\n\u001b[0;32m     41\u001b[0m app\u001b[38;5;241m.\u001b[39madd_handler(MessageHandler(filters\u001b[38;5;241m.\u001b[39mCOMMAND, unknown))  \u001b[38;5;66;03m# Filters out unknown commands\u001b[39;00m\n\u001b[1;32m---> 43\u001b[0m app\u001b[38;5;241m.\u001b[39mrun_polling()\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\telegram\\ext\\_application.py:871\u001b[0m, in \u001b[0;36mApplication.run_polling\u001b[1;34m(self, poll_interval, timeout, bootstrap_retries, read_timeout, write_timeout, connect_timeout, pool_timeout, allowed_updates, drop_pending_updates, close_loop, stop_signals)\u001b[0m\n\u001b[0;32m    868\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21merror_callback\u001b[39m(exc: TelegramError) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    869\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mcreate_task(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprocess_error(error\u001b[38;5;241m=\u001b[39mexc, update\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[1;32m--> 871\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m__run(\n\u001b[0;32m    872\u001b[0m     updater_coroutine\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mupdater\u001b[38;5;241m.\u001b[39mstart_polling(\n\u001b[0;32m    873\u001b[0m         poll_interval\u001b[38;5;241m=\u001b[39mpoll_interval,\n\u001b[0;32m    874\u001b[0m         timeout\u001b[38;5;241m=\u001b[39mtimeout,\n\u001b[0;32m    875\u001b[0m         bootstrap_retries\u001b[38;5;241m=\u001b[39mbootstrap_retries,\n\u001b[0;32m    876\u001b[0m         read_timeout\u001b[38;5;241m=\u001b[39mread_timeout,\n\u001b[0;32m    877\u001b[0m         write_timeout\u001b[38;5;241m=\u001b[39mwrite_timeout,\n\u001b[0;32m    878\u001b[0m         connect_timeout\u001b[38;5;241m=\u001b[39mconnect_timeout,\n\u001b[0;32m    879\u001b[0m         pool_timeout\u001b[38;5;241m=\u001b[39mpool_timeout,\n\u001b[0;32m    880\u001b[0m         allowed_updates\u001b[38;5;241m=\u001b[39mallowed_updates,\n\u001b[0;32m    881\u001b[0m         drop_pending_updates\u001b[38;5;241m=\u001b[39mdrop_pending_updates,\n\u001b[0;32m    882\u001b[0m         error_callback\u001b[38;5;241m=\u001b[39merror_callback,  \u001b[38;5;66;03m# if there is an error in fetching updates\u001b[39;00m\n\u001b[0;32m    883\u001b[0m     ),\n\u001b[0;32m    884\u001b[0m     close_loop\u001b[38;5;241m=\u001b[39mclose_loop,\n\u001b[0;32m    885\u001b[0m     stop_signals\u001b[38;5;241m=\u001b[39mstop_signals,\n\u001b[0;32m    886\u001b[0m )\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\telegram\\ext\\_application.py:1099\u001b[0m, in \u001b[0;36mApplication.__run\u001b[1;34m(self, updater_coroutine, stop_signals, close_loop)\u001b[0m\n\u001b[0;32m   1097\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m   1098\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m close_loop:\n\u001b[1;32m-> 1099\u001b[0m         loop\u001b[38;5;241m.\u001b[39mclose()\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\asyncio\\proactor_events.py:686\u001b[0m, in \u001b[0;36mBaseProactorEventLoop.close\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    684\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mclose\u001b[39m(\u001b[38;5;28mself\u001b[39m):\n\u001b[0;32m    685\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_running():\n\u001b[1;32m--> 686\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCannot close a running event loop\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    687\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mis_closed():\n\u001b[0;32m    688\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m\n",
      "\u001b[1;31mRuntimeError\u001b[0m: Cannot close a running event loop"
     ]
    }
   ],
   "source": [
    "from telegram import Update\n",
    "from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext\n",
    "\n",
    "async def start(update: Update, context: CallbackContext):\n",
    "    await update.message.reply_text(\"Hello sir, Welcome to the Bot. Please write\")\n",
    "\n",
    "async def help_command(update: Update, context: CallbackContext):\n",
    "    await update.message.reply_text(\"\"\"Available Commands :-\n",
    "    /youtube - To get the youtube URL\n",
    "    /linkedin - To get the LinkedIn profile URL\n",
    "    /gmail - To get gmail URL\n",
    "    /geeks - To get the GeeksforGeeks URL\"\"\")\n",
    "\n",
    "async def gmail_url(update: Update, context: CallbackContext):\n",
    "    await update.message.reply_text(\"Your gmail link here: \")\n",
    "\n",
    "async def youtube_url(update: Update, context: CallbackContext):\n",
    "    await update.message.reply_text(\"Youtube Link => https://www.youtube.com/\")\n",
    "\n",
    "async def linkedin_url(update: Update, context: CallbackContext):\n",
    "    await update.message.reply_text(\"LinkedIn URL => https://www.linkedin.com/in/dwaipayan-bandyopadhyay-007a/\")\n",
    "\n",
    "async def geeks_url(update: Update, context: CallbackContext):\n",
    "    await update.message.reply_text(\"GeeksforGeeks URL => https://www.geeksforgeeks.org/\")\n",
    "\n",
    "async def unknown(update: Update, context: CallbackContext):\n",
    "    await update.message.reply_text(\"Sorry '%s' is not a valid command\" % update.message.text)\n",
    "\n",
    "async def unknown_text(update: Update, context: CallbackContext):\n",
    "    await update.message.reply_text(\"Sorry I can't recognize you, you said '%s'\" % update.message.text)\n",
    "\n",
    "app = ApplicationBuilder().token(\"your_own_API_Token got from BotFather\").build()\n",
    "\n",
    "app.add_handler(CommandHandler('start', start))\n",
    "app.add_handler(CommandHandler('youtube', youtube_url))\n",
    "app.add_handler(CommandHandler('help', help_command))\n",
    "app.add_handler(CommandHandler('linkedin', linkedin_url))\n",
    "app.add_handler(CommandHandler('gmail', gmail_url))\n",
    "app.add_handler(CommandHandler('geeks', geeks_url))\n",
    "app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown_text))\n",
    "app.add_handler(MessageHandler(filters.COMMAND, unknown))  # Filters out unknown commands\n",
    "\n",
    "app.run_polling()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "db2a66ec-60c1-475a-b5df-f6fb069987c2",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'Updater' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m updater \u001b[38;5;241m=\u001b[39m Updater(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myour_own_API_Token got from BotFather\u001b[39m\u001b[38;5;124m\"\u001b[39m, \n\u001b[0;32m      2\u001b[0m                   use_context\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m) \n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mstart\u001b[39m(update: Update, context: CallbackContext): \n\u001b[0;32m      6\u001b[0m \tupdate\u001b[38;5;241m.\u001b[39mmessage\u001b[38;5;241m.\u001b[39mreply_text(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mHello, welcome, how may I help you?\u001b[39m\u001b[38;5;124m\"\u001b[39m) \n",
      "\u001b[1;31mNameError\u001b[0m: name 'Updater' is not defined"
     ]
    }
   ],
   "source": [
    "updater = Updater(\"your_own_API_Token got from BotFather\", \n",
    "                  use_context=True) \n",
    "\n",
    "\n",
    "def start(update: Update, context: CallbackContext): \n",
    "\tupdate.message.reply_text(\"Hello, welcome, how may I help you?\") \n",
    "\n",
    "def help(update: Update, context: CallbackContext): \n",
    "\tupdate.message.reply_text(\"Your Message\") \n",
    "\n",
    "def gmail_url(update: Update, context: CallbackContext): \n",
    "\tupdate.message.reply_text(\"gmail link here\") \n",
    "\n",
    "\n",
    "def youtube_url(update: Update, context: CallbackContext): \n",
    "\tupdate.message.reply_text(\"youtube link\") \n",
    "\n",
    "\n",
    "def linkedIn_url(update: Update, context: CallbackContext): \n",
    "\tupdate.message.reply_text(\"Your linkedin profile url\") \n",
    "\n",
    "\n",
    "def geeks_url(update: Update, context: CallbackContext): \n",
    "\tupdate.message.reply_text(\"GeeksforGeeks url here\") \n",
    "\n",
    "\n",
    "def unknown_text(update: Update, context: CallbackContext): \n",
    "\tupdate.message.reply_text( \n",
    "\t\t\"Sorry I can't recognize you , you said '%s'\" % update.message.text) \n",
    "\n",
    "\n",
    "def unknown(update: Update, context: CallbackContext): \n",
    "\tupdate.message.reply_text( \n",
    "\t\t\"Sorry '%s' is not a valid command\" % update.message.text) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1305ccf5-0425-448d-92a7-c1e4e7181ef6",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'updater' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[6], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m updater\u001b[38;5;241m.\u001b[39mdispatcher\u001b[38;5;241m.\u001b[39madd_handler(CommandHandler(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstart\u001b[39m\u001b[38;5;124m'\u001b[39m, start)) \n\u001b[0;32m      2\u001b[0m updater\u001b[38;5;241m.\u001b[39mdispatcher\u001b[38;5;241m.\u001b[39madd_handler(CommandHandler(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124myoutube\u001b[39m\u001b[38;5;124m'\u001b[39m, youtube_url)) \n\u001b[0;32m      3\u001b[0m updater\u001b[38;5;241m.\u001b[39mdispatcher\u001b[38;5;241m.\u001b[39madd_handler(CommandHandler(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mhelp\u001b[39m\u001b[38;5;124m'\u001b[39m, help)) \n",
      "\u001b[1;31mNameError\u001b[0m: name 'updater' is not defined"
     ]
    }
   ],
   "source": [
    "updater.dispatcher.add_handler(CommandHandler('start', start)) \n",
    "updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url)) \n",
    "updater.dispatcher.add_handler(CommandHandler('help', help)) \n",
    "updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url)) \n",
    "updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url)) \n",
    "updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url)) \n",
    "updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown)) \n",
    "updater.dispatcher.add_handler(MessageHandler( \n",
    "\t# Filters out unknown commands \n",
    "\tFilters.command, unknown)) \n",
    "\n",
    "# Filters out unknown messages. \n",
    "updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ddeec938-9097-45ed-b26d-9eaaf103a02a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
