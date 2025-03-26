# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qbanet <qbanet@student.42perpignan.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/26 12:42:30 by qbanet            #+#    #+#              #
#    Updated: 2025/03/26 12:55:45 by qbanet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
import time

date = datetime.date.today()
formatedDate = date.strftime("%b %d %Y")

hour = time.gmtime()

print(f"Seconds since January 1, 1970: {time.time():.2f} or {time.time():.2e} in scientific notation")
print(f"{formatedDate}")