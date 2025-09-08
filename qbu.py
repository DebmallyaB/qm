from manim import *
import numpy as np

class BlochSphereScene(ThreeDScene):
    def construct(self):
        # Add title and qubit definition
        title = Text("Bloch Sphere & Qubit", font_size=48)
        qubit_def = Text("A qubit is a quantum bit that can be in superposition of |0⟩ and |1⟩", 
                        font_size=32)
        
        self.add_fixed_in_frame_mobjects(title, qubit_def)
        title.to_corner(UL)
        qubit_def.next_to(title, DOWN)
        
        # Create Bloch sphere
        sphere = Sphere(radius=1, resolution=(15, 32), fill_opacity=0.5, color=BLUE)
        
        # Add axes
        axes = ThreeDAxes()
        labels = VGroup(
            Text("|0⟩").move_to(axes.c2p(0, 0, 1.2)),
            Text("|1⟩").move_to(axes.c2p(0, 0, -1.2)),
            Text("|+⟩").move_to(axes.c2p(1.2, 0, 0)),
            Text("|-⟩").move_to(axes.c2p(-1.2, 0, 0)),
        )
        
        # Create state vector
        state_vector = Arrow(
            start=ORIGIN,
            end=[1, 0, 1],
            color=YELLOW,
            buff=0,
            max_tip_length_to_length_ratio=0.2,
            stroke_width=8,
        )
        
        # Add everything to scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        
        self.play(
            Create(sphere),
            Create(axes),
            Write(labels),
            GrowArrow(state_vector)
        )
        
        # Demonstrate superposition by rotating state vector
        self.play(
            Rotate(
                state_vector,
                angle=2*PI,
                axis=UP,
                about_point=ORIGIN,
                run_time=4
            )
        )
        
        self.wait(2)

        # Add explanation
        explanation = Text(
            "A qubit can point to any direction on the Bloch sphere,\n"
            "representing quantum superposition",
            font_size=24
        ).to_corner(DR)
        self.add_fixed_in_frame_mobjects(explanation)
        
        self.wait(2)