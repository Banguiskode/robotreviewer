"""
RobotReviewer tokenizer
"""
import logging
log = logging.getLogger(__name__)

log.debug('Loading spacy.io data for tokenization')
from spacy.en import English
nlp = English()