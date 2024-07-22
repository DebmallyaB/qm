from manim import *

class SemiconductorTransition(Scene):
    def construct(self):
        # Title
        title = Text("Semiconductor Transition", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Draw bands
        valence_band = Rectangle(width=6, height=1, color=BLUE, fill_opacity=0.5).shift(DOWN)
        conduction_band = Rectangle(width=6, height=1, color=RED, fill_opacity=0.5).shift(UP)
        self.play(Create(valence_band), Create(conduction_band))

        # Labels
        vb_label = Text("Valence Band", font_size=24).next_to(valence_band, LEFT)
        cb_label = Text("Conduction Band", font_size=24).next_to(conduction_band, LEFT)
        self.play(Write(vb_label), Write(cb_label))

        # Electrons in the valence band
        electrons = VGroup(*[
            Dot(point=[x, -1, 0], color=YELLOW)
            for x in [-2, -1, 0, 1, 2]
        ])
        self.play(FadeIn(electrons))

        # Electron transition
        transition_arrow = Arrow(start=electrons[2].get_center(), end=[0, 1, 0], buff=0.1, color=GREEN)
        self.play(GrowArrow(transition_arrow))
        self.play(electrons[2].animate.shift(UP*2))

        # Electron in conduction band
        cb_electron = Dot(point=[0, 1, 0], color=YELLOW)
        self.play(ReplacementTransform(electrons[2], cb_electron))

        self.wait(2)
