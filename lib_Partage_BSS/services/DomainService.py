# -*-coding:utf-8 -*
"""
Module contenant les méthodes permettant d'appeler les services de l'API BSS concernant les domaines
"""
import re
from collections import OrderedDict
from time import time

from lib_Partage_BSS import models, utils, services
from lib_Partage_BSS.exceptions import NameException, DomainException, ServiceException
from .GlobalService import callMethod


def getDomain(domain):
    """
    Méthode permettant de récupérer les informations d'un domaine via l'API BSS

    :return: Les informations sur le domaine
    :raises ServiceException: Exception levée si la requête vers l'API à echoué. L'exception contient le code de l'erreur et le message
    :raises NameException: Exception levée si le nom n'est pas une adresse mail valide
    :raises DomainException: Exception levée si le domaine de l'adresse mail n'est pas un domaine valide
    """

    data = {
    }
    response = callMethod(domain, "GetDomain", data)
    if utils.checkResponseStatus(response["status"]):
        domain = response["domain"]
        return domain
    elif re.search(".*no such domain.*", response["message"]):
        return None
    else:
        raise ServiceException(response["status"], response["message"])

def countObjects(domain, type):
    """
    Méthode permettant de récupérer le nombre d'objets (userAccount, alias, dl, calresource) d'un domaine via l'API BSS

    :return: Le nombre d'objets dans le domaine
    :raises ServiceException: Exception levée si la requête vers l'API à echoué. L'exception contient le code de l'erreur et le message
    :raises NameException: Exception levée si le nom n'est pas une adresse mail valide
    :raises DomainException: Exception levée si le domaine de l'adresse mail n'est pas un domaine valide
    """

    data = {
        "type": type
    }
    response = callMethod(domain, "CountObjects", data)
    if utils.checkResponseStatus(response["status"]):
        count = response["count"]["content"]
        return count
    elif re.search(".*no such domain.*", response["message"]):
        return None
    else:
        raise ServiceException(response["status"], response["message"])


