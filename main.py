from manim import *

class Proof(Scene):
    def construct(self):
        # constants
        RADIUS = 2
        ANGLE_RADIUS = 0.5
        SHIFT_MULTIPLIER = 4

        # draw the grid
        dot = Dot(ORIGIN)
        numberplane = NumberPlane().set_opacity(0.5)
        origin_text = Text('(0, 0)').next_to(dot, DOWN).scale(0.5)
        self.play(FadeIn(numberplane, dot))
        self.wait()
        self.play(Write(origin_text))
        self.wait()

        # draw the unit circle
        circle = Circle(RADIUS, WHITE)
        self.play(DrawBorderThenFill(circle))
        self.wait()
        
        t = Tex("This is a unit circle").shift(UP * 3)
        self.play(Write(t))
        self.wait()
        self.play(Unwrite(t))

        # configure the angle
        theta_tracker = ValueTracker(1)
        starting_line = Line(ORIGIN, RIGHT * RADIUS)
        line = Arrow(ORIGIN, np.array([RADIUS, 0, 0]), buff=0)
        line_ref = line.copy()
        line.rotate(theta_tracker.get_value() * DEGREES, about_point=ORIGIN)
        a = Angle(starting_line, line, radius=ANGLE_RADIUS, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(starting_line, line, radius=ANGLE_RADIUS + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5)
        )
        pos = MathTex(r"(\sin\theta, \cos\theta)").next_to(line.get_end(), UP).scale(0.5)
        self.play(FadeIn(starting_line, line, a, tex, pos))
        self.wait()

        # initialize updaters
        line.add_updater(
            lambda x: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=ORIGIN
            )
        )

        a.add_updater(lambda x: x.become(Angle(starting_line, line, radius=ANGLE_RADIUS, other_angle=False)))

        tex.add_updater(
            lambda x: x.move_to(
                Angle(starting_line, line, radius=ANGLE_RADIUS + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5)
            )
        )

        pos.add_updater(
            lambda x: x.next_to(line.get_end(), UP * 2)
        )

        # play animation
        self.play(theta_tracker.animate.set_value(140))
        self.wait()
        self.play(theta_tracker.animate.increment_value(-100))
        self.wait()

        self.play(FadeOut(starting_line, line, a, tex, pos))
        self.wait()

        # first angle
        line1 = Arrow(ORIGIN, [RADIUS, 0, 0], buff=0).rotate_about_origin(40 * DEGREES).set_color(RED)
        tex1 = MathTex(r"\theta_1").move_to(
            Angle(starting_line, line1, radius=ANGLE_RADIUS + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5)
        ).scale(0.5).set_color(RED)
        pos1 = MathTex(r"(\sin\theta_1, \cos\theta_1)").next_to(line1.get_end(), RIGHT * 0.5).scale(0.5).set_color(RED)
        a1 = Angle(starting_line, line1, radius=ANGLE_RADIUS * 0.9, other_angle=False).set_color(RED)
 
        self.play(FadeIn(line1, tex1, pos1, a1))
        self.wait()

        # second angle
        line2 = Arrow(ORIGIN, [RADIUS, 0, 0], buff=0).rotate_about_origin(120 * DEGREES).set_color(BLUE)
        tex2 = MathTex(r"\theta_2").move_to(
            Angle(starting_line, line2, radius=ANGLE_RADIUS + 3 * SMALL_BUFF, other_angle=False).point_from_proportion(0.5)
        ).scale(0.5).set_color(BLUE)
        pos2 = MathTex(r"(\sin\theta_2, \cos\theta_2)").next_to(line2.get_end(), UP).scale(0.5).set_color(BLUE)
        a2 = Angle(starting_line, line2, radius=ANGLE_RADIUS * 1.1, other_angle=False).set_color(BLUE)
 
        self.play(FadeIn(line2, tex2, pos2, a2))
        self.wait()

        self.play(FadeOut(numberplane, origin_text))
        self.wait()

        # draw triangle
        triangle = Polygon(dot.get_end(), line1.get_end(), line2.get_end()).set_color(PURPLE).set_opacity(0.5)
        self.play(DrawBorderThenFill(triangle))
        self.wait()
        self.play(triangle.animate.scale(0.5).center().shift(UP * 3))
        self.wait()

        # write equations for the area
        eq1 = MathTex(r"\frac{1}{2}\cdot1\cdot1\sin(\theta_2 - \theta_1)=").scale(0.5).shift(UP * 3).shift(LEFT * 2)
        eq2 = MathTex(
        r"=\frac{1}{2}\begin{vmatrix} 0 & \cos\theta_1 & \cos\theta_2 & 0 \\ 0 &  \sin\theta_1& \sin\theta_2 & 0 \end{vmatrix}"
        ).scale(0.5).shift(UP * 3).shift(RIGHT * 2)
        equations = VGroup(eq1, eq2)
        self.play(Write(equations))
        self.wait()

        eq = MathTex(r"\frac{1}{2}\cdot1\cdot1\sin(\theta_2 - \theta_1)=\frac{1}{2}\begin{vmatrix} 0 & \cos\theta_1 & \cos\theta_2 & 0 \\ 0 &  \sin\theta_1& \sin\theta_2 & 0 \end{vmatrix}").scale(0.5)
        eq_1 = MathTex(r"\sin(\theta_2 - \theta_1)=\left| [0\cdot\sin\theta_1+\cos\theta_1\sin\theta_2+\cos\theta_2\cdot0]-[0\cdot\cos\theta_1+\sin\theta_1\cos\theta_2+\sin\theta_2\cdot0] \right|").scale(0.5)
        eq_2= MathTex(r"\sin(\theta_2 - \theta_1)=\cos\theta_1\sin\theta_2-\sin\theta_1\cos\theta_2").scale(0.5)

        # general equations
        gn_eq_1 = MathTex(r"\sin(a - b)=\sin a\cos b-\sin b\cos a").shift(UP * 2)

        gn_eq_2_1 = MathTex(r"\sin(a + b)=sin(a-(-b))").shift(UP)
        gn_eq_2_2 = MathTex(r"\sin(a + b)=\sin a\cos (-b)-\sin (-b)\cos a").shift(UP)
        gn_eq_2_3 = MathTex(r"\sin(a + b)=\sin a\cos b+\sin b\cos a").shift(UP)

        gn_eq_3_1 = MathTex(r"\cos(a + b)=\sin(90 - a - b)").shift(DOWN)
        gn_eq_3_2 = MathTex(r"\cos(a + b)=\sin (90-a)\cos b-\sin b\cos (90-a)").shift(DOWN)
        gn_eq_3_3 = MathTex(r"\cos(a + b)=\cos a\cos b-\sin b\sin a").shift(DOWN)

        gn_eq_4_1 = MathTex(r"\cos(a - b)=\sin(90-a+b)").shift(DOWN * 2)
        gn_eq_4_2 = MathTex(r"\cos(a - b)=\sin(90-a)\cos b+\sin b \cos(90-a)").shift(DOWN * 2)
        gn_eq_4_3 = MathTex(r"\cos(a - b)=\cos a\cos b+\sin b \sin a").shift(DOWN * 2)
        
        self.play(FadeOut(
        triangle, dot, circle, line1, line2, tex1, tex2, a1, a2, pos1, pos2
        ))
        self.play(equations.animate.become(eq))
        self.wait()
        self.add(eq)
        self.remove(equations)
        self.play(TransformMatchingTex(eq, eq_1))
        self.wait()
        self.play(TransformMatchingTex(eq_1, eq_2))
        self.wait()
        self.play(TransformMatchingShapes(eq_2, gn_eq_1))
        self.wait()
        self.play(TransformFromCopy(gn_eq_1, gn_eq_2_1))
        self.play(TransformFromCopy(gn_eq_1, gn_eq_3_1))
        self.play(TransformFromCopy(gn_eq_1, gn_eq_4_1))
        self.wait()
        self.play(TransformMatchingTex(gn_eq_2_1, gn_eq_2_2))
        self.play(TransformMatchingTex(gn_eq_3_1, gn_eq_3_2))
        self.play(TransformMatchingTex(gn_eq_4_1, gn_eq_4_2))
        self.wait()
        self.play(TransformMatchingTex(gn_eq_2_2, gn_eq_2_3))
        self.play(TransformMatchingTex(gn_eq_3_2, gn_eq_3_3))
        self.play(TransformMatchingTex(gn_eq_4_2, gn_eq_4_3))
        self.wait()

