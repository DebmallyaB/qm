from manim import *

class QubitIntro(Scene):
    def construct(self):
        # Title
        title = Text("What is a Qubit?", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Step 1: Classical Bit
        bit_box = Square(color=BLUE).shift(LEFT*3)
        bit_text = Text("Bit", font_size=32).next_to(bit_box, UP)
        bit_values = Text("0 or 1", font_size=28).move_to(bit_box.get_center())
        self.play(Create(bit_box), Write(bit_text))
        self.play(Write(bit_values))
        self.wait(1)

        # Step 2: Transition to Qubit
        arrow = Arrow(start=bit_box.get_right(), end=RIGHT*0.5, buff=0.5, color=WHITE)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Step 3: Qubit
        qubit_box = Square(color=GREEN).shift(RIGHT*3)
        qubit_text = Text("Qubit", font_size=32).next_to(qubit_box, UP)
        qubit_values = Text("Superposition\nof 0 and 1", font_size=28, gradient=(BLUE, GREEN)).move_to(qubit_box.get_center())
        self.play(Create(qubit_box), Write(qubit_text))
        self.play(Write(qubit_values))
        self.wait(2)

        # Step 4: Highlight Information Storage
        info_text = Text("This is how we store\ninformation in quantum computing",
                         font_size=28, color=YELLOW).next_to(qubit_box, DOWN*2)
        self.play(Write(info_text))
        self.wait(3)
