import pytest

try:
    from playwright.sync_api import expect
except ImportError:
    pytestmark = pytest.mark.skip("playwright not available")

pytestmark = pytest.mark.ui

from panel import Column, Spacer
from panel.layout.gridstack import GridStack
from panel.tests.util import serve_component


def test_gridstack(page):
    gspec = GridStack(width=800, height=600, margin=0)

    gspec[:, 0] = Spacer(styles=dict(background="red"))
    gspec[0, 1:3] = Spacer(styles=dict(background="green"))
    gspec[1, 2:4] = Spacer(styles=dict(background="orange"))
    gspec[2, 1:4] = Spacer(styles=dict(background="blue"))
    gspec[0:1, 3:4] = Spacer(styles=dict(background="purple"))

    serve_component(page, gspec)

    children = page.locator(".grid-stack > div > div > div")

    expect(children).to_have_count(5)

    bbox = page.locator(".grid-stack").bounding_box()

    assert bbox["width"] == 800
    assert bbox["height"] == 600
    bbox1 = children.nth(0).bounding_box()
    assert bbox1["x"] == 0
    assert bbox1["width"] == 200
    assert bbox1["height"] == 600
    assert (
        children.nth(0).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(255, 0, 0)"
    )
    bbox2 = children.nth(1).bounding_box()
    assert bbox2["x"] == 200
    assert bbox2["y"] == 0
    assert bbox2["width"] == 400
    assert bbox2["height"] == 200
    assert (
        children.nth(1).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(0, 128, 0)"
    )
    bbox3 = children.nth(2).bounding_box()
    assert bbox3["x"] == 400
    assert bbox3["y"] == 200
    assert bbox3["width"] == 400
    assert bbox3["height"] == 200
    assert (
        children.nth(2).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(255, 165, 0)"
    )
    bbox4 = children.nth(3).bounding_box()
    assert bbox4["x"] == 200
    assert bbox4["y"] == 400
    assert bbox4["width"] == 600
    assert bbox4["height"] == 200
    assert (
        children.nth(3).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(0, 0, 255)"
    )
    bbox5 = children.nth(4).bounding_box()
    assert bbox5["x"] == 600
    assert bbox5["y"] == 0
    assert bbox5["width"] == 200
    assert bbox5["height"] == 200
    assert (
        children.nth(4).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(128, 0, 128)"
    )

    gspec[1, 1] = Spacer(styles=dict(background="black"))

    children = page.locator(".grid-stack > div > div > div")

    expect(children).to_have_count(6)
    page.wait_for_timeout(500)

    assert (
        children.nth(5).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(0, 0, 0)"
    )
    bbox6 = children.nth(5).bounding_box()
    assert bbox6["x"] == 200
    assert bbox6["y"] == 200
    assert bbox6["width"] == 200
    assert bbox6["height"] == 200


def test_gridstack_stretch(page):
    gspec = GridStack(sizing_mode="stretch_both")
    column = Column(gspec, max_width=800, max_height=600)

    gspec[:, 0] = Spacer(styles=dict(background="red"))
    gspec[0, 1:3] = Spacer(styles=dict(background="green"))
    gspec[1, 2:4] = Spacer(styles=dict(background="orange"))
    gspec[2, 1:4] = Spacer(styles=dict(background="blue"))
    gspec[0:1, 3:4] = Spacer(styles=dict(background="purple"))

    serve_component(page, column)

    children = page.locator(".grid-stack > div > div > div")

    expect(children).to_have_count(5)

    bbox = page.locator(".grid-stack").bounding_box()

    assert bbox["width"] == 800
    assert bbox["height"] == 600
    bbox1 = children.nth(0).bounding_box()
    assert bbox1["x"] == 0
    assert bbox1["width"] == 200
    assert bbox1["height"] == 600
    assert (
        children.nth(0).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(255, 0, 0)"
    )
    bbox2 = children.nth(1).bounding_box()
    assert bbox2["x"] == 200
    assert bbox2["y"] == 0
    assert bbox2["width"] == 400
    assert bbox2["height"] == 200
    assert (
        children.nth(1).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(0, 128, 0)"
    )
    bbox3 = children.nth(2).bounding_box()
    assert bbox3["x"] == 400
    assert bbox3["y"] == 200
    assert bbox3["width"] == 400
    assert bbox3["height"] == 200
    assert (
        children.nth(2).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(255, 165, 0)"
    )
    bbox4 = children.nth(3).bounding_box()
    assert bbox4["x"] == 200
    assert bbox4["y"] == 400
    assert bbox4["width"] == 600
    assert bbox4["height"] == 200
    assert (
        children.nth(3).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(0, 0, 255)"
    )
    bbox5 = children.nth(4).bounding_box()
    assert bbox5["x"] == 600
    assert bbox5["y"] == 0
    assert bbox5["width"] == 200
    assert bbox5["height"] == 200
    assert (
        children.nth(4).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(128, 0, 128)"
    )

    gspec[1, 1] = Spacer(styles=dict(background="black"))

    children = page.locator(".grid-stack > div > div > div")

    expect(children).to_have_count(6)

    page.wait_for_timeout(500)

    assert (
        children.nth(5).evaluate(
            """(element) =>
        window.getComputedStyle(element).getPropertyValue('background-color')"""
        )
        == "rgb(0, 0, 0)"
    )
    bbox6 = children.nth(5).bounding_box()
    assert bbox6["x"] == 200
    assert bbox6["y"] == 200
    assert bbox6["width"] == 200
    assert bbox6["height"] == 200
