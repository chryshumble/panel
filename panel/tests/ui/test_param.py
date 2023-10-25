import time

import pytest

try:
    from playwright.sync_api import expect

    pytestmark = pytest.mark.ui
except ImportError:
    pytestmark = pytest.mark.skip("playwright not available")

from panel.pane import panel
from panel.tests.util import serve_component


def test_param_defer_load(page):
    def defer_load():
        time.sleep(0.5)
        return "I render after load!"

    component = panel(defer_load, defer_load=True)

    serve_component(page, component)

    assert page.locator(".pn-loading")

    expect(page.locator(".markdown").locator("div")).to_have_text("I render after load!\n")
