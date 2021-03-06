## GHOST DOG BATTLE - START

# Default battle screen, where the player chooses which move to use
if current == "choose ability":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)

    if mousein(960,430,1100,540):
        screen.blit(kick_move_icon_faded, (960,390))
        screen.blit(headbutt_move_icon_faded, (1010,390))
        screen.blit(frostbeam_move_icon_faded, (1060,390))

        if left and not display_options:
            current = "aggressive moves"
            
    elif mousein(135,380,235,520):
        screen.blit(heal_move_icon_faded, (165,330))

        if left and not display_options:
            current = "defensive moves"

# Screen showing the player their aggressive move options
elif current == "aggressive moves":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
    
    screen.blit(kick_move_icon_solid, (960,390))
    screen.blit(headbutt_move_icon_solid, (1010,390))
    screen.blit(frostbeam_move_icon_solid, (1060,390))

    if mousein(960,390,1000,430):
        screen.blit(kick_move_info, (930,130))
    elif mousein(1010,390,1050,430):
        screen.blit(headbutt_move_info, (930,130))
    elif mousein(1060,390,1100,430):
        screen.blit(frostbeam_move_info, (930,130))
    
    if left and not display_options:
        if mousein(960,390,1000,430):
            character_current_mana += 10
            if character_current_mana > character_max_mana:
                character_current_mana = character_max_mana
            display_mana_notification_time = 2*fps
            current = "kick move"
        elif mousein(1010,390,1050,430):
            if character_current_mana >= 20:
                character_current_mana -= 20
                display_mana_notification_time = 2*fps
                current = "headbutt move"
            else:
                display_mana_notification_time = 0
        elif mousein(1060,390,1100,430):
            if character_current_mana >= 30:
                character_current_mana -= 30
                display_mana_notification_time = 2*fps
                current = "frostbeam move"
            else:
                display_mana_notification_time = 0
        elif not mousein(930,380,1130,540):
            current = "choose ability"

# Screen showing the player their defensive move options
elif current == "defensive moves":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
    
    screen.blit(heal_move_icon_solid, (165,330))

    if mousein(165,330,205,370):
        screen.blit(heal_move_info, (220,130))

    if left and not display_options:
        if mousein(165,330,205,370):
            if character_current_mana >= 10:
                character_current_mana -= 10
                display_mana_notification_time = 2*fps
                current = "heal move"
            else:
                display_mana_notification_time = 0
        elif not mousein(150,320,220,560):
            current = "choose ability"

# Not enough mana screen - displays text telling the player that they do not have enough mana to use the move they tried to use
elif current == "ghost_dog_not_enough_mana":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)

    if duration_time < 2*fps:
        screen.blit(not_enough_mana, (300,200))
        duration_time += 1
    else:
        current = "choose ability"
        duration_time = 0

# Ghost Dog dead/Victory screen
elif current == "ghost dog dead":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    screen.blit(ghost_dog_dead, (930,440))
    screen.blit(victory_overlay, (0,0))
    screen.blit(continue_button, (1000,600))
    screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

    if left and not display_options:
        if mousein(1000,600,1120,650):
            current = "title"           # NEEDS CHANGING
            character_level += 1
##            current = "choose ability"         ### CHANGE THIS WHEN CLOUD BATTLE IS COMPLETE
##            opponent_name = "Spook Cloud"   (Doesn't have to be called this, change below too though if you do change it)      
##            character_level += 1
##            character_max_hp = 90 + 10*int(character_level)
##            character_current_hp = 90 + 10*int(character_level)
##            character_max_mana = 95 + 5*int(character_level)
##            character_current_mana = 95 + 5*int(character_level)
##            enemy_max_hp = 180
##            enemy_current_hp = 180
##            enemy_max_mana = 300
##            enemy_current_mana = 300
            savegame(save_number)
        elif mousein(80,600,268,650):
            #opponent_name = "Spook Cloud" ##SHOULD BE THIS, UNCOMMENT WHEN COMPLETED##
            character_level += 1
            savegame(save_number)
            current = "title"

# Character dead/Defeat screen
elif current == "character dead":
    screen.blit(character_dead, (150,480))
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
    screen.blit(defeat_overlay, (0,0))
    screen.blit(try_again_button, (1000,600))
    screen.blit(return_to_title_button, (80,600))   # Stopping the return to title button being faded out by the overlay

    if left and not display_options:
        if mousein(1000,600,1200,700):
            current = "choose ability"       # Change this if you make something to happen after the first (and only) fight
            character_level += 0.25
            character_max_hp = 90 + 10*int(character_level)
            character_current_hp = 90 + 10*int(character_level)
            character_max_mana = 95 + 5*int(character_level)
            character_current_mana = 95 + 5*int(character_level)
            enemy_max_hp = 200
            enemy_current_hp = 200
            enemy_max_mana = 150
            enemy_current_mana = 150
            savegame(save_number)
        elif mousein(80,600,268,650):
            savegame(save_number)
            current = "title"

## Character moves

# Character heal move animation
elif current == "heal move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)

    if heal_heart_y < 350:
        if heal_heart_y == 170:
            heal_move_sound()
        screen.blit(heal_heart, (160,heal_heart_y))
        heal_heart_y += 5

    else:
        if not healed_already:
            healed_by = random.randint(5,15)
            if character_current_hp + healed_by > character_max_hp:
                healed_by = character_max_hp - character_current_hp
            character_current_hp += healed_by
            display_healed = font.render("+" + str(healed_by), True, HEAL_GREEN)
            healed_already = True

        if duration_time < fps/2:
            screen.blit(display_healed, (170, display_healed_y))
            duration_time += 1
            display_healed_y -= 3
        else:
            # Resetting variables for next time
            heal_heart_y = 170
            display_healed_y = 360
            duration_time = 0
            healed_already = False
            ghost_dog_next_move = choose_ghost_dog_move()
            enemy_current_mana = ghost_dog_change_mana(enemy_current_mana,ghost_dog_next_move)
            current = ghost_dog_next_move

# Character kick move animation
elif current == "kick move":
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
    
    if advancing:
        if character_kick_x == 150:
            character_stage = idle_movement(character_stage,character_number,20,150,380)
            character_kick_x += 24
        elif character_kick_x < 870:
            if character_tilt_direction == "left":
                screen.blit(character_tilt_left, (character_kick_x,380))
                character_tilt_direction = "right"
            elif character_tilt_direction == "right":
                screen.blit(character_tilt_right, (character_kick_x,380))
                character_tilt_direction =  "left"
            character_kick_x += 24
            if character_kick_x == 750:
                character_attack_sound()
                
        elif character_kick_x == 870:
            screen.blit(character_tilt_left, (870,380))
            kick_damage = random.randint(8,12)
            if enemy_current_hp - kick_damage < 0:
                kick_damage = enemy_current_hp
            enemy_current_hp -= kick_damage                        
            display_damage = font.render("-" + str(kick_damage), True, DAMAGE_RED)
            display_damage_time = 0
            character_kick_x -= 36
            advancing = False
            
    elif not advancing:
        if character_kick_x > 150:
            character_stage = idle_movement(character_stage,character_number,20,character_kick_x,380)
            character_kick_x -= 36
        else:
            # Resetting variables for next time
            advancing = True
            character_kick_x = 150
            character_tilt_direction = "left"
            display_damage_y = 420
            if enemy_current_hp == 0:
                current = "ghost dog dead"
            else:
                ghost_dog_next_move = choose_ghost_dog_move()
                enemy_current_mana = ghost_dog_change_mana(enemy_current_mana,ghost_dog_next_move)
                current = ghost_dog_next_move

    if display_damage_time < fps/2:     # Make this into a function in the future? if more battles are made (also for the heal one)
        screen.blit(display_damage, (1015,display_damage_y))
        display_damage_time += 1
        display_damage_y -= 3
    else:
        display_damage_time = fps

# Character headbutt move animation
elif current == "headbutt move":
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
    
    if advancing:
        if character_headbutt_x == 150:
            character_stage = idle_movement(character_stage,character_number,20,150,380)
            character_headbutt_x += 24
        elif character_headbutt_x < 870:
            screen.blit(character_headbutt_stance, (character_headbutt_x,380))
            character_headbutt_x += 24
            if character_headbutt_x == 750:
                character_attack_sound()
                
        elif character_headbutt_x == 870:
            screen.blit(character_headbutt_stance, (870,380))
            headbutt_damage = random.randint(10,20)
            if enemy_current_hp - headbutt_damage < 0:
                headbutt_damage = enemy_current_hp
            enemy_current_hp -= headbutt_damage                        
            display_damage = font.render("-" + str(headbutt_damage), True, DAMAGE_RED)
            display_damage_time = 0
            character_headbutt_x -= 36
            advancing = False
            
    elif not advancing:
        if character_headbutt_x > 150:
            character_stage = idle_movement(character_stage,character_number,20,character_headbutt_x,380)
            character_headbutt_x -= 36
        else:
            # Resetting variables for next time
            advancing = True
            character_headbutt_x = 150
            display_damage_y = 420
            if enemy_current_hp == 0:
                current = "ghost dog dead"
            else:
                ghost_dog_next_move = choose_ghost_dog_move()
                enemy_current_mana = ghost_dog_change_mana(enemy_current_mana,ghost_dog_next_move)
                current = ghost_dog_next_move

    if display_damage_time < fps/2:
        screen.blit(display_damage, (1015,display_damage_y))
        display_damage_time += 1
        display_damage_y -= 3
    else:
        display_damage_time = fps
        
# Character frostbeam move animation
elif current == "frostbeam move":
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
    screen.blit(character_frostbeam_stance, (150,380))

    if duration_time < 2*fps:
        if duration_time == 0:
            frostbeam_move_sound()
        elif duration_time == fps:
            frostbeam_damage = random.randint(15,30)
            if enemy_current_hp - frostbeam_damage < 0:
                frostbeam_damage = enemy_current_hp
            enemy_current_hp -= frostbeam_damage                        
            display_damage = font.render("-" + str(frostbeam_damage), True, DAMAGE_RED)
            display_damage_time = 0
            
        screen.blit(frostbeam_start, (215,381))
        screen.blit(frostbeam_middle, (265,383))
        screen.blit(frostbeam_middle, (315,385))
        screen.blit(frostbeam_middle, (365,387))
        screen.blit(frostbeam_middle, (415,389))
        screen.blit(frostbeam_middle, (465,391))
        screen.blit(frostbeam_middle, (515,393))
        screen.blit(frostbeam_middle, (565,395))
        screen.blit(frostbeam_middle, (615,397))
        screen.blit(frostbeam_middle, (665,399))
        screen.blit(frostbeam_middle, (715,401))
        screen.blit(frostbeam_middle, (765,403))
        screen.blit(frostbeam_middle, (815,405))
        screen.blit(frostbeam_middle, (865,407))
        screen.blit(frostbeam_middle, (915,409))
        duration_time += 1

    
    else:
        # Resetting variables for next time
        display_damage_time = fps
        duration_time = 0
        if enemy_current_hp == 0:
                current = "ghost dog dead"
        else:

            ghost_dog_next_move = choose_ghost_dog_move()
            enemy_current_mana = ghost_dog_change_mana(enemy_current_mana,ghost_dog_next_move)
            current = ghost_dog_next_move

    if display_damage_time < fps/2:
        screen.blit(display_damage, (1015,display_damage_y))
        display_damage_time += 1
        display_damage_y -= 3

## Ghost Dog moves

# Ghost dog heal move animation
elif current == "ghost dog heal move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)

    if enemy_heal_y < 410:
        if enemy_heal_y == 230:
            heal_move_sound()
        screen.blit(heal_heart, (1005,enemy_heal_y))
        enemy_heal_y += 5

    else:
        if not healed_already:
            healed_by = random.randint(5,20)
            if enemy_current_hp + healed_by > enemy_max_hp:
                healed_by = enemy_max_hp - enemy_current_hp
            enemy_current_hp += healed_by
            display_healed = font.render("+" + str(healed_by), True, HEAL_GREEN)
            healed_already = True

        if duration_time < fps/2:
            screen.blit(display_healed, (1015, display_healed_y))
            duration_time += 1
            display_healed_y -= 3
        else:
            # Resetting variables for next time
            enemy_heal_y = 170
            display_healed_y = 360
            duration_time = 0
            healed_already = False
            current = "choose ability"

# Ghost dog glide move animation
elif current == "ghost dog glide move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)

    if ghost_dog_glide_x == 690:
        glide_move_sound()

    ghost_dog_glide_x -= 24
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,ghost_dog_glide_x,(440+int(200*math.sin(((float((ghost_dog_glide_x - 210)/2))*math.pi)/float(180)))))

    if ghost_dog_glide_x == 210:
        glide_damage = random.randint(20,30)
        if character_current_hp - glide_damage < 0:
            glide_damage = character_current_hp
        character_current_hp -= glide_damage
        display_damage = font.render("-" + str(glide_damage), True, DAMAGE_RED)
        display_damage_time = 0

    if ghost_dog_glide_x <= -6:
        ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,1296+ghost_dog_glide_x,(440+int(200*math.sin(((float((ghost_dog_glide_x - 210)/4))*math.pi)/float(180)))))

    if ghost_dog_glide_x == -366:
        ghost_dog_glide_x = 930
        if character_current_hp == 0:
            current = "character dead"
        else:
            current = "choose ability"
                
    if display_damage_time < fps/2:
        screen.blit(display_damage, (170,character_display_damage_y))
        display_damage_time += 1
        character_display_damage_y -= 3
    else:
        character_display_damage_y = 360
        display_damage_time = fps

# Ghost dog teleport move animation
elif current == "ghost dog teleport move":
    character_stage = idle_movement(character_stage,character_number,20,150,380)
    if not started_glowing:
        duration_time = 2*fps
        teleport_move_sound()
        started_glowing = True

    if duration_time != 0:
        ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
        if duration_time % 10 > 5:
            glow_phase = 5 - (duration_time % 5)
        elif duration_time % 10 == 0:
            glow_phase = 0
        elif duration_time % 10 < 5:
            glow_phase = duration_time % 5
        else:
            glow_phase = 5
            
        if glow_phase == 1:
            screen.blit(ghost_dog_glow1, (830,290))
        elif glow_phase == 2:
            screen.blit(ghost_dog_glow2, (830,290))
        elif glow_phase == 3:
            screen.blit(ghost_dog_glow3, (830,290))
        elif glow_phase == 4:
            screen.blit(ghost_dog_glow4, (830,290))
        elif glow_phase == 5:
            screen.blit(ghost_dog_glow5, (830,290))
        else:   # (when glow_phase = 0)
            ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
        duration_time -= 1

    elif ghost_dog_attack_time != 0:
        ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,220,380)
        ghost_dog_attack_time -= 1

        if not damage_decided:        
            teleport_damage = random.randint(1,20)
            if character_current_hp - teleport_damage < 0:
                teleport_damage = character_current_hp
            character_current_hp -= teleport_damage
            display_damage = font.render("-" + str(teleport_damage), True, DAMAGE_RED)

            if character_current_mana < 10:
                mana_damage = character_current_mana
            else:
                mana_damage = 10
            character_current_mana -= mana_damage
            mana_damage = font.render("-" + str(mana_damage), True, MANA_BLUE)
            display_damage_time = 0
            damage_decided = True        
            
    else:
        started_glowing = False
        damage_decided = False
        ghost_dog_attack_time = fps/2
        if character_current_hp == 0:
            current = "character dead"
        else:
            current = "choose ability"      

    if display_damage_time < ((fps/2)+8):
        if display_damage_time < fps/2:
            screen.blit(display_damage, (170,character_display_damage_y))
            display_damage_time += 1
        character_display_damage_y -= 3
        if character_display_damage_y > 21:
            screen.blit(mana_damage, (170,character_display_damage_y + 24))
    else:
        character_display_damage_y = 360
        display_damage_time = fps
    
# Ghost dog claw move animation
elif current == "ghost dog claw move":
    screen.blit(character_normal, (150,380))
    ghost_dog_stage = idle_movement(ghost_dog_stage,"ghost_dog",20,930,440)
    
    if opacity < 100 and fade_direction == "out" and not already_clawed:
        opacity = fade(fade_direction,opacity)
        screen.blit(character_normal, (150,380))
        if opacity == 100:
            duration_time = 2*fps
            fade_direction = "in"
    else:
        if duration_time > 0:
            screen.fill(BLACK)

            if duration_time == fps:
                claw_move_sound()

            if duration_time < fps:
                if (duration_time < fps and duration_time > fps-6) or (duration_time < fps-10 and duration_time > fps-16):
                    screen.blit(character_scared_redflash, (150,380))
                else:
                    screen.blit(character_scared, (150,380))

                if duration_time > fps-6:    
                    if duration_time == fps-1:                        
                        screen.blit(ghost_dog_top_claw_swipe1, (145,365))
                    elif duration_time == fps-2:
                        screen.blit(ghost_dog_top_claw_swipe2, (145,365))
                    elif duration_time == fps-3:
                        screen.blit(ghost_dog_top_claw_swipe3, (145,365))
                    elif duration_time == fps-4:
                        screen.blit(ghost_dog_top_claw_swipe4, (145,365))
                    elif duration_time == fps-5:
                        screen.blit(ghost_dog_top_claw_swipe5, (145,365))

                elif duration_time > fps-11:
                    if duration_time == fps-6:
                        screen.blit(ghost_dog_top_claw_size1, (145,365))
                    elif duration_time == fps-7:
                        screen.blit(ghost_dog_top_claw_size2, (145,365))
                    elif duration_time == fps-8:
                        screen.blit(ghost_dog_top_claw_size3, (145,365))
                    elif duration_time == fps-9:
                        screen.blit(ghost_dog_top_claw_size4, (145,365))
                    elif duration_time == fps-10:
                        screen.blit(ghost_dog_top_claw_size5, (145,365))

                elif duration_time > fps-18:                
                    if duration_time == fps-11:
                        screen.blit(ghost_dog_top_claw_size6, (145,365))
                        screen.blit(ghost_dog_side_claw_swipe1, (130,420))
                    elif duration_time == fps-12:
                        screen.blit(ghost_dog_top_claw_size7, (145,365))
                        screen.blit(ghost_dog_side_claw_swipe2, (130,420))
                    elif duration_time == fps-13:
                        screen.blit(ghost_dog_top_claw_size8, (145,365))
                        screen.blit(ghost_dog_side_claw_swipe3, (130,420))
                    elif duration_time == fps-14:
                        screen.blit(ghost_dog_top_claw_fade80, (145,365))
                        screen.blit(ghost_dog_side_claw_swipe4, (130,420))
                    elif duration_time == fps-15:
                        screen.blit(ghost_dog_top_claw_fade60, (145,365))
                        screen.blit(ghost_dog_side_claw_swipe5, (130,420))
                    elif duration_time == fps-16:
                        screen.blit(ghost_dog_top_claw_fade40, (145,365))
                        screen.blit(ghost_dog_side_claw_size1, (130,420))
                    elif duration_time == fps-17:
                        screen.blit(ghost_dog_top_claw_fade20, (145,365))
                        screen.blit(ghost_dog_side_claw_size2, (130,420))
                 
                elif duration_time == fps-18:
                    screen.blit(ghost_dog_side_claw_size3, (130,420))
                elif duration_time == fps-19:
                    screen.blit(ghost_dog_side_claw_size4, (130,420))
                elif duration_time == fps-20:
                    screen.blit(ghost_dog_side_claw_size5, (130,420))
                elif duration_time == fps-21:
                    screen.blit(ghost_dog_side_claw_size6, (130,420))
                elif duration_time == fps-22:
                    screen.blit(ghost_dog_side_claw_size7, (130,420))
                elif duration_time == fps-23:
                    screen.blit(ghost_dog_side_claw_size8, (130,420))
                elif duration_time == fps-24:
                    screen.blit(ghost_dog_side_claw_fade80, (130,420))
                elif duration_time == fps-25:
                    screen.blit(ghost_dog_side_claw_fade60, (130,420))
                elif duration_time == fps-26:
                    screen.blit(ghost_dog_side_claw_fade40, (130,420))
                elif duration_time == fps-27:
                    screen.blit(ghost_dog_side_claw_fade20, (130,420))            

            else:
                screen.blit(character_scared, (150,380))
                
            duration_time -= 1
            
            if duration_time == 0:
                claw_damage = random.randint(10,60)
                if character_current_hp - claw_damage < 0:
                    claw_damage = character_current_hp
                character_current_hp -= claw_damage
                display_damage = font.render("-" + str(claw_damage), True, DAMAGE_RED)
                display_damage_time = 0
                
        else:
            if opacity > 0 and not already_clawed:
                opacity = fade(fade_direction,opacity)
                screen.blit(character_scared, (150,380))
                if opacity == 0:
                    opacity = 10
                    fade_direction = "out"
                    already_clawed = True             
                    
            if display_damage_time < fps/2:
                screen.blit(display_damage, (170,character_display_damage_y))
                display_damage_time += 1
                character_display_damage_y -= 3
            else:
                character_display_damage_y = 360
                display_damage_time = fps
                already_clawed = False

                if character_current_hp == 0:
                    current = "character dead"
                else:
                    current = "choose ability"             

# GHOST DOG BATTLE - END
