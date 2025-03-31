# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qbanet <qbanet@student.42perpignan.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/31 11:45:36 by qbanet            #+#    #+#              #
#    Updated: 2025/03/31 12:06:27 by qbanet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
    exit()
assert len(sys.argv) == 2, "more than one argument is provided"
assert sys.argv[1].lstrip('-').isdigit(), "argument is not an integer"

number = int(sys.argv[1])
if number % 2 == 0:
	print("I'm Even.")
elif number:
	print("I'm Odd")