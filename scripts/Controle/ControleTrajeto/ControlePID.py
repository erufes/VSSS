import time
from IControleTrajeto import IcontroleTrajeto


class ControleTrajetoPID(IcontroleTrajeto):
    def __init__(self, pid_P: float = 0.2, pid_I: float = 0.0, pid_D: float = 0.0, current_time: float = None):
        """Determines how aggressively the PID reacts to the current error with setting Proportional Gain"""
        self._kp = pid_P
        """Determines how aggressively the PID reacts to the current error with setting Integral Gain"""
        self._ki = pid_I
        """Determines how aggressively the PID reacts to the current error with setting Derivative Gain"""
        self._kd = pid_D

        self._sample_time = 0.00
        self._current_time = current_time if current_time is not None else time.time()
        self._last_time = self.current_time

        self.clear()

    def clear(self):
        """Clears PID computations and coefficients"""
        self.SetPoint = 0.0

        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.lastError = 0.0

        # Windup Guard
        self.intError = 0.0
        self.windupGuard = 20.0

        self.output = 0.0

    def controle(self, actualValue):
        pass
        """ xs, ys, ts = start
        xg, yg, tg = goal
        erroT = ts - tg
        erroX = xs - xg
        erroY = ys - yg """

    def update(self, feedback_value, current_time=None):
        """ Calculates PID value for given reference feedback
            Test PID with kp=1.2, ki=1, kd=0.001 (test_pid.py)
        """
        error = self.SetPoint - feedback_value

        self.current_time = current_time if current_time is not None else time.time()
        delta_time = self.current_time - self.last_time
        deltaError = error - self.lastError

        if (delta_time >= self.sample_time):
            self.PTerm = self.kp * error
            self.ITerm += error * delta_time

            if (self.ITerm < -self.windupGuard):
                self.ITerm = -self.windupGuard
            elif (self.ITerm > self.windupGuard):
                self.ITerm = self.windupGuard

            self.DTerm = 0.0
            if delta_time > 0:
                self.DTerm = deltaError / delta_time

            # Remember last time and last error for next calculation
            self.last_time = self.current_time
            self.lastError = error

            self.output = self.PTerm + \
                (self._ki * self.ITerm) + (self.kd * self.DTerm)

    def setWindup(self, windup):
        """ Integral windup, also known as integrator windup or reset windup,
            refers to the situation in a PID feedback controller where
            a large change in setpoint occurs (say a positive change)
            and the integral terms accumulates a significant error
            during the rise (windup), thus overshooting and continuing
            to increase as this accumulated error is unwound
            (offset by errors in the other direction).
            The specific problem is the excess overshooting.
        """
        self.windupGuard = windup

    def setSampleTime(self, sample_time):
        """ PID that should be updated at a regular interval.
            Based on a pre-determined sampe time, the PID decides
            if it should compute or return immediately.
        """
        self.sample_time = sample_time
