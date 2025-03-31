# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qbanet <qbanet@student.42perpignan.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/26 13:48:04 by qbanet            #+#    #+#              #
#    Updated: 2025/03/31 11:41:38 by qbanet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
	oType = type(object)

	if isinstance(object, bool) and not object:
		print(f"Fake : {object} <class '{oType.__name__}'>")

	elif isinstance(object, float) and object != object:
		print(f"Cheese : {object} <class '{oType.__name__}'>")

	elif not object:
		match object:
			case None:
				print(f"Nothing : {object} <class '{oType.__name__}'>")
			case 0:
				print(f"Zero : {object} <class '{oType.__name__}'>")
			case "":
				print(f"Empty : {object} <class '{oType.__name__}'>")

	else:
		print("Type not Found")
		return 1

	return 0