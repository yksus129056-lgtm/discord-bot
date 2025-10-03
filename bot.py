import discord
from discord.ui import View, Button
import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# База данных для хранения описаний
описания = {
    # WK UP (новый бренд)
    "WK UP - Тропик": "🌀 **Тропик (Tropic)**\n\nСмесь тропических фруктов: манго, маракуйя, ананас\n\n💬 *Освежающий тропический микс*",
    "WK UP - Кола": "🌀 **Кола (Cherry Cola)**\n\nВкус, напоминающий классическую колу\n\n⭐ **Оценка: 7.5/10**\n💬 *Отличный баланс сладости и газации*",
    "WK UP - Лимон-Лайм": "🌀 **Лимон-Лайм (Lemon-Lime)**\n\nОсвежающий цитрусовый вкус, похожий на Sprite или 7Up\n\n💬 *Идеален для освежения*",
    "WK UP - Фруктовый пунш": "🌀 **Фруктовый пунш (Fruit Punch)**\n\nСладкая смесь различных красных ягод и фруктов\n\n⭐ **Оценка: 4/10**\n💬 *Слишком сладкий для некоторых*",
    "WK UP - Грейпфрут": "🌀 **Грейпфрут (Grapefruit)**\n\nГорьковато-сладкий, освежающий вкус\n\n💬 *Бодрящая горчинка*",
    "WK UP - Маракуйя": "🌀 **Маракуйя (Passion Fruit)**\n\nЯркий и сладкий тропический вкус\n\n💬 *Экзотический и насыщенный*",
    "WK UP - Малина": "🌀 **Малина (Raspberry)**\n\nЯгодный, слегка терпкий вкус\n\n⭐ **Оценка: 4/10**\n💬 *На любителя*",
    
    # Red Bull
    "Red Bull - Классический": "🔴 **Классический энергетик**\n\n💬 *Описание скоро появится*",
    "Red Bull - Без сахара": "🔴 **Без сахара**\n\n💬 *Описание скоро появится*",
    "Red Bull - Тропические фрукты": "🔴 **Тропические фрукты**\n\n💬 *Описание скоро появится*",
    "Red Bull - Грейпфрут": "🔴 **Грейпфрут**\n\n💬 *Описание скоро появится*",
    
    # Monster
    "Monster - Классический": "👹 **Классический**\n\n💬 *Описание скоро появится*",
    "Monster - Ультра": "👹 **Ультра (без сахара)**\n\n💬 *Описание скоро появится*",
    "Monster - Манго Локо": "👹 **Манго Локо**\n\n💬 *Описание скоро появится*",
    "Monster - Ассаулт": "👹 **Ассаулт**\n\n💬 *Описание скоро появится*",
    
    # Burn
    "Burn - Классический": "🔥 **Классический**\n\n💬 *Описание скоро появится*",
    "Burn - Цитро": "🔥 **Цитро**\n\n💬 *Описание скоро появится*",
    "Burn - Апельсин-Манго": "🔥 **Апельсин-Манго**\n\n💬 *Описание скоро появится*",
    "Burn - Без сахара": "🔥 **Без сахара**\n\n💬 *Описание скоро появится*",
}

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

# Главное меню
class ГлавноеМеню(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="🍽️ Съестное", style=discord.ButtonStyle.primary, emoji="🍽️")
    async def еда_кнопка(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюЕды())
    
    @discord.ui.button(label="🥤 Напитки", style=discord.ButtonStyle.success, emoji="🥤")
    async def напитки_кнопка(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюНапитков())

# Меню еды
class МенюЕды(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="🍔 Mak.by", style=discord.ButtonStyle.primary, emoji="🍔")
    async def мак(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🍔 Mak.by", description="Фастфуд ресторан", color=0xffd700)
        embed.add_field(name="🍟 Популярное", value="• Биг Мак\n• Чизбургер\n• МакЧикен\n• Картофель фри\n• Наггетсы", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="🍗 KFC", style=discord.ButtonStyle.danger, emoji="🍗")
    async def кфс(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="🍗 KFC", description="Куриный фастфуд", color=0xff0000)
        embed.add_field(name="🍗 Популярное", value="• Баскет\n• Стрипсы\n• Бургеры\n• Картофель\n• Крылышки", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="👑 Burger King", style=discord.ButtonStyle.success, emoji="👑")
    async def бургер_кинг(self, interaction: discord.Interaction, button: Button):
        embed = discord.Embed(title="👑 Burger King", description="Бургер ресторан", color=0xff8c00)
        embed.add_field(name="🍔 Популярное", value="• Воппер\n• Чизбургер\n• Лонгер\n• Кинг фри\n• Наггетсы", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="🔙 Назад", style=discord.ButtonStyle.gray, emoji="🔙")
    async def назад_кнопка(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=ГлавноеМеню())

# Меню напитков
class МенюНапитков(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="⚡ Энергетики", style=discord.ButtonStyle.secondary, emoji="⚡")
    async def энергетики_кнопка(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюЭнергетиков())
    
    @discord.ui.button(label="🔙 Назад", style=discord.ButtonStyle.gray, emoji="🔙")
    async def назад_кнопка(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=ГлавноеМеню())

# Меню энергетиков
class МенюЭнергетиков(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="🌀 WK UP", style=discord.ButtonStyle.primary, emoji="🌀")
    async def вкап(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюВкусовWKUP())
    
    @discord.ui.button(label="🔴 Red Bull", style=discord.ButtonStyle.primary)
    async def редбулл(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюВкусовRedBull())
    
    @discord.ui.button(label="👹 Monster", style=discord.ButtonStyle.primary)
    async def монстр(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюВкусовMonster())
    
    @discord.ui.button(label="🔥 Burn", style=discord.ButtonStyle.primary)
    async def берн(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюВкусовBurn())
    
    @discord.ui.button(label="🔙 Назад", style=discord.ButtonStyle.gray, emoji="🔙")
    async def назад_кнопка(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюНапитков())

# Меню вкусов WK UP
class МенюВкусовWKUP(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Тропик", style=discord.ButtonStyle.primary)
    async def тропик(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("WK UP - Тропик", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🌀 WK UP - Тропик", description=описание, color=0xff9900)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Кола", style=discord.ButtonStyle.primary)
    async def кола(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("WK UP - Кола", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🌀 WK UP - Кола", description=описание, color=0x8B4513)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Лимон-Лайм", style=discord.ButtonStyle.primary)
    async def лимон_лайм(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("WK UP - Лимон-Лайм", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🌀 WK UP - Лимон-Лайм", description=описание, color=0x00ff00)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Фруктовый пунш", style=discord.ButtonStyle.primary)
    async def пунш(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("WK UP - Фруктовый пунш", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🌀 WK UP - Фруктовый пунш", description=описание, color=0xff0066)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Грейпфрут", style=discord.ButtonStyle.primary)
    async def грейпфрут(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("WK UP - Грейпфрут", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🌀 WK UP - Грейпфрут", description=описание, color=0xff6b6b)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Маракуйя", style=discord.ButtonStyle.primary)
    async def маракуйя(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("WK UP - Маракуйя", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🌀 WK UP - Маракуйя", description=описание, color=0xffcc00)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Малина", style=discord.ButtonStyle.primary)
    async def малина(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("WK UP - Малина", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🌀 WK UP - Малина", description=описание, color=0xff1493)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="🔙 Назад", style=discord.ButtonStyle.gray)
    async def назад(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюЭнергетиков())

# Меню вкусов Red Bull
class МенюВкусовRedBull(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Классический", style=discord.ButtonStyle.primary)
    async def классический(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("Red Bull - Классический", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🔴 Red Bull - Классический", description=описание, color=0xff0000)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Без сахара", style=discord.ButtonStyle.success)
    async def без_сахара(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("Red Bull - Без сахара", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🔴 Red Bull - Без сахара", description=описание, color=0x00ff00)
        embed.add_field(name="🍭 Сахар", value="Без сахара", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="🔙 Назад", style=discord.ButtonStyle.gray)
    async def назад(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюЭнергетиков())

# Меню вкусов Monster
class МенюВкусовMonster(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Классический", style=discord.ButtonStyle.primary)
    async def классический(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("Monster - Классический", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="👹 Monster - Классический", description=описание, color=0x00ff00)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Ультра", style=discord.ButtonStyle.success)
    async def ультра(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("Monster - Ультра", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="👹 Monster - Ультра", description=описание, color=0xffffff)
        embed.add_field(name="🍭 Сахар", value="Без сахара", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="🔙 Назад", style=discord.ButtonStyle.gray)
    async def назад(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюЭнергетиков())

# Меню вкусов Burn
class МенюВкусовBurn(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Классический", style=discord.ButtonStyle.primary)
    async def классический(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("Burn - Классический", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🔥 Burn - Классический", description=описание, color=0xff6b6b)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="Цитро", style=discord.ButtonStyle.primary)
    async def цитро(self, interaction: discord.Interaction, button: Button):
        описание = описания.get("Burn - Цитро", "💬 *Описание скоро появится*")
        embed = discord.Embed(title="🔥 Burn - Цитро", description=описание, color=0xffff00)
        embed.add_field(name="🍭 Сахар", value="Содержит сахар", inline=True)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @discord.ui.button(label="🔙 Назад", style=discord.ButtonStyle.gray)
    async def назад(self, interaction: discord.Interaction, button: Button):
        await interaction.response.edit_message(view=МенюЭнергетиков())

@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user} успешно запущен!')
    print('💬 Напишите "!меню" в чате')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    if message.content == "!меню":
        view = ГлавноеМеню()
        embed = discord.Embed(
            title="🍽️ Меню еды и напитков",
            description="Выберите категорию ниже 👇",
            color=0x7289da
        )
        await message.channel.send(embed=embed, view=view)
    
    # Важная строка для обработки событий
    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_TOKEN'))