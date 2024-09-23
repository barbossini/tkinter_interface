# test_interface.py

import pytest
import interface

def test_display_message():
    # Test simulé pour vérifier l'affichage du message
    assert interface.display_message("Test Message") is None
