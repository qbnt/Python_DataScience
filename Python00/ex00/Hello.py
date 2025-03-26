# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: qbanet <qbanet@student.42perpignan.fr>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/26 12:41:22 by qbanet            #+#    #+#              #
#    Updated: 2025/03/26 12:41:23 by qbanet           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


ft_list[ft_list.index("tata!")] = "World!"
ft_tuple = (ft_tuple[0], "France!")
ft_set.remove("tutu!")
ft_set.add("Perpignan!")
ft_dict["Hello"] = "42Perpignan Occitanie!"

print(ft_list)
print(ft_tuple)
print(ft_set) #Impossible de garentir l'ordre des éléments
print(ft_dict)