import simpylc as sp

class Timing (sp.Chart):
    def __init__ (self):
        sp.Chart.__init__ (self)
        
    def define (self):
        self.channel (sp.world.robot.torEnab, sp.white)
        self.channel (sp.world.robot.torVolt, sp.red, -10, 10, 20)
        self.channel (sp.world.robot.torAng, sp.red, -220, 220, 70)
        self.channel (sp.world.robot.torBrake, sp.red)
        
        self.channel (sp.world.robot.uppEnab, sp.white)
        self.channel (sp.world.robot.uppVolt, sp.lime, -10, 10, 20)
        self.channel (sp.world.robot.uppAng, sp.lime, -110, 110, 35)
        self.channel (sp.world.robot.uppBrake, sp.lime)
        
        self.channel (sp.world.robot.forEnab, sp.white)
        self.channel (sp.world.robot.forVolt, sp.blue, -10, 10, 20)
        self.channel (sp.world.robot.forAng, sp.blue, -110, 110, 35)
        self.channel (sp.world.robot.forBrake, sp.blue)

        self.channel (sp.world.robot.wriEnab, sp.white)
        self.channel (sp.world.robot.wriVolt, sp.yellow, -10, 10, 20)
        self.channel (sp.world.robot.wriAng, sp.yellow, -110, 110, 35)
        self.channel (sp.world.robot.wriBrake, sp.yellow)
        
        self.channel (sp.world.robot.hanEnab, sp.white)
        self.channel (sp.world.robot.hanAng, sp.aqua, -110, 110, 35)
        
        self.channel (sp.world.robot.finEnab, sp.white)
        self.channel (sp.world.robot.finAng, sp.fuchsia, -55, 55, 35)
        
                
