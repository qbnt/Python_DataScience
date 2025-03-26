# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qbanet <qbanet@student.42perpignan.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/26 12:56:38 by qbanet            #+#    #+#              #
#    Updated: 2025/03/26 13:45:45 by qbanet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
	if object:
		oType = type(object).__name__
		nameType = oType.capitalize()
		if oType == "str":
			print(f"{ object } is in the kitchen: <class '{nameType}'>")
		elif oType == "int":
			print("Type not found")
		else:
			print(f"{nameType} : <class '{ type(object).__name__ }'>")
	return 42
