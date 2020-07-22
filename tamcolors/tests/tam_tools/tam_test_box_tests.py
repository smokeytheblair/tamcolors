# built in libraries
import unittest.mock

# tamcolors libraries
from tamcolors import tam_io
from tamcolors import tam_tools


class TAMTextBoxTests(unittest.TestCase):
    def test_tam_text_box_init(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertIsInstance(text_box, tam_tools.tam_text_box.TAMTextBox)

    def test_tam_text_box_str(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(str(text_box), "hello world!")

    def test_tam_text_box_str_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("cat world!\n123", 20, 34, "#", 3, 5)
        self.assertEqual(str(text_box), "cat world!\n123")

    def test_update(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("", 20, 15, "#", 3, 5)

        buffer = tam_io.tam_buffer.TAMBuffer(20, 15, " ", 3, 5)
        buffer2 = tam_io.tam_buffer.TAMBuffer(20, 15, "@", 1, 2)
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

        for i in range(20):
            buffer.set_spot(i, 0, "#", 3, 5)
            buffer.set_spot(i, 14, "#", 3, 5)

        for i in range(1, 15):
            buffer.set_spot(0, i, "#", 3, 5)
            buffer.set_spot(19, i, "#", 3, 5)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

    def test_draw(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 15, "#", 3, 5)
        buffer = tam_io.tam_buffer.TAMBuffer(20, 15, " ", 3, 5)
        buffer2 = tam_io.tam_buffer.TAMBuffer(20, 15, "@", 1, 2)
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

        for i in range(20):
            buffer.set_spot(i, 0, "#", 3, 5)
            buffer.set_spot(i, 14, "#", 3, 5)

        for i in range(1, 15):
            buffer.set_spot(0, i, "#", 3, 5)
            buffer.set_spot(19, i, "#", 3, 5)

        for spot, char in enumerate("hello world!"):
            buffer.set_spot(2 + spot, 7, char, 3, 5)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

    def test_draw_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 15, "#", 3, 5, clock=1)
        buffer = tam_io.tam_buffer.TAMBuffer(20, 15, " ", 3, 5)
        buffer2 = tam_io.tam_buffer.TAMBuffer(20, 15, "@", 1, 2)
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

        for i in range(20):
            buffer.set_spot(i, 0, "#", 3, 5)
            buffer.set_spot(i, 14, "#", 3, 5)

        for i in range(1, 15):
            buffer.set_spot(0, i, "#", 3, 5)
            buffer.set_spot(19, i, "#", 3, 5)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)
        for spot, char in enumerate("hello world!"):
            buffer.set_spot(2 + spot, 7, char, 3, 5)
            text_box.update()
            text_box.draw(buffer2)
            self.assertEqual(buffer, buffer2)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

    def test_draw_3(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!\ncats\n1\n\nhi",
                                                     19,
                                                     16,
                                                     "#",
                                                     1,
                                                     2,
                                                     center_vertical=False,
                                                     center_horizontal=True,
                                                     vertical_space=2,
                                                     vertical_start=3,
                                                     char_background="%")

        buffer = tam_io.tam_buffer.TAMBuffer(19, 16, "%", 1, 2)
        buffer2 = tam_io.tam_buffer.TAMBuffer(19, 16, "@", 3, 4)

        for i in range(19):
            buffer.set_spot(i, 0, "#", 1, 2)
            buffer.set_spot(i, 15, "#", 1, 2)

        for i in range(1, 16):
            buffer.set_spot(0, i, "#", 1, 2)
            buffer.set_spot(18, i, "#", 1, 2)

        for spot, char in enumerate("hello world!"):
            buffer.set_spot(3 + spot, 3, char, 1, 2)

        for spot, char in enumerate("cats"):
            buffer.set_spot(7 + spot, 5, char, 1, 2)

        buffer.set_spot(9, 7, "1", 1, 2)

        for spot, char in enumerate("hi"):
            buffer.set_spot(8 + spot, 11, char, 1, 2)

        text_box.update()
        text_box.draw(buffer2)
        self.assertEqual(buffer, buffer2)

    def test_done(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertFalse(text_box.done())
        text_box.update()
        self.assertTrue(text_box.done())

    def test_done_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5, clock=1)
        for _ in range(14):
            self.assertFalse(text_box.done())
            text_box.update()
        self.assertTrue(text_box.done())

    def test_set_colors(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertFalse(text_box.done())
        text_box.update()
        self.assertTrue(text_box.done())
        text_box.set_colors(4, 6)
        self.assertTrue(text_box.done())

    def test_set_colors_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5, clock=1)
        for _ in range(14):
            self.assertFalse(text_box.done())
            text_box.update()

        self.assertTrue(text_box.done())
        text_box.set_colors(4, 6)
        self.assertTrue(text_box.done())

    def test_set_colors_3(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5, clock=1)
        for _ in range(13):
            self.assertFalse(text_box.done())
            text_box.update()

        self.assertFalse(text_box.done())
        text_box.set_colors(4, 6)
        self.assertFalse(text_box.done())

    def test_get_colors(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_colors(), (3, 5))

    def test_get_colors_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 6, 1)
        self.assertEqual(text_box.get_colors(), (6, 1))

    def test_set_char(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "^", 3, 5)
        text_box.set_char("#")
        self.assertEqual(text_box.get_char(), "#")

    def test_set_char_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "@", 6, 1)
        text_box.set_char("$")
        self.assertEqual(text_box.get_char(), "$")

    def test_get_char(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_char(), "#")

    def test_get_char_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "!", 6, 1)
        self.assertEqual(text_box.get_char(), "!")

    def test_get_text(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_text(), "hello world!")

    def test_get_text_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("cat world!\n123", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_text(), "cat world!\n123")

    def test_get_dimensions(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 20, 34, "#", 3, 5)
        self.assertEqual(text_box.get_dimensions(), (20, 34))

    def test_get_dimensions_2(self):
        text_box = tam_tools.tam_text_box.TAMTextBox("hello world!", 4, 3, "#", 3, 5)
        self.assertEqual(text_box.get_dimensions(), (4, 3))
