import pytest

try:
    from playwright.sync_api import expect

    pytestmark = pytest.mark.ui
except ImportError:
    pytestmark = pytest.mark.skip("playwright not available")

from panel.pane import Markdown
from panel.template import MaterialTemplate
from panel.tests.util import serve_component


def test_material_template_no_console_errors(page):
    tmpl = MaterialTemplate()
    md = Markdown("Initial")

    tmpl.main.append(md)

    msgs, _ = serve_component(page, tmpl)

    expect(page.locator(".markdown").locator("div")).to_have_text("Initial\n")

    assert [msg for msg in msgs if msg.type == "error"] == []


def test_material_template_updates(page):
    tmpl = MaterialTemplate()
    md = Markdown("Initial")

    tmpl.main.append(md)

    serve_component(page, tmpl)

    expect(page.locator(".markdown").locator("div")).to_have_text("Initial\n")
    md.object = "Updated"
    expect(page.locator(".markdown").locator("div")).to_have_text("Updated\n")
