from pyze.api import GigyaAsync, Kamereon, KamereonAsync

import getpass
import aiohttp


help_text = 'Log in to your MY Renault account.'


async def run(args):
    email = input('Enter your My Renault email address: ')
    if email == '':
        return
    password = getpass.getpass('Enter your password: ')
    if password == '':
        return

    async with aiohttp.ClientSession() as websession:
        g = GigyaAsync(websession=websession)
        if await g.login(email, password):
            await g.account_info()

            k = KamereonAsync(gigya=g, websession=websession)
            accounts = await k.get_accounts()
            if len(accounts) > 1:
                Kamereon.print_multiple_account_warning(accounts)

                print('Logged in successfully.')
        else:
            print('Failed to log in!')
