#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_serverless_exceptions
----------------------------------

Tests for `serverless_exceptions` module.
"""

import string
import random
import pytest
from pytest import raises, fixture, mark
from serverless_exceptions import *


@fixture()
def description():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(40))


EXCEPTION_LIST = [BadRequest, Unauthorized, Forbidden, NotFound, MethodNotAllowed, NotAcceptable, RequestTimeout,
                  Conflict, Gone, LengthRequired, PreconditionFailed, RequestEntityTooLarge, RequestURITooLarge,
                  UnsupportedMediaType, RequestedRangeNotSatisfiable, ExpectationFailed, ImATeapot, UnprocessableEntity,
                  PreconditionRequired, TooManyRequests, RequestHeaderFieldsTooLarge, InternalServerError,
                  NotImplemented, BadGateway, ServiceUnavailable, GatewayTimeout, HTTPVersionNotSupported]


@pytest.mark.parametrize('custom_exception', EXCEPTION_LIST)
def test_exception_with_custom_description(description, custom_exception):
    with raises(ServerlessHTTPException) as ex:
        raise custom_exception(description)
    assert str(ex.value).startswith('[%s]' % custom_exception.code)
    assert description in str(ex.value)


@pytest.mark.parametrize('custom_exception', EXCEPTION_LIST)
def test_exception_with_default_description(custom_exception):
    with raises(ServerlessHTTPException) as ex:
        raise custom_exception()
    assert str(ex.value).startswith('[%s]' % custom_exception.code)
    assert custom_exception.description in str(ex.value)
