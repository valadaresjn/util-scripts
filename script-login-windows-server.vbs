'Script de Login


On error Resume Next
Err.clear 0

'============================================================================
'Mapeando Unidades de Disco

Set WshNetwork = Wscript.CreateObject("Wscript.Network")
WshNetwork.MapNetworkDrive "Z:","\\SHARED\FOLDER$","true"

'============================================================================
'Sincroniza o horario da estacao com o servidor

Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2")
Set objShell = CreateObject("WScript.shell")
strCmd = "net time \\nemeserver /set /yes"
set objexec = objshell.exec(strcmd)

'============================================================================
'Boas Vindas Ao Usuario

Set objUser = WScript.CreateObject("WScript.Network")
wuser=objUser.UserName
If Time <= "12:00:00" Then
MsgBox ("Bom Dia "+Wuser+", você acaba de ingressar na rede corporativa, por favor respeite as políticas de segurança e bom trabalho!")
ElseIf Time >= "12:00:01" And Time <= "18:00:00" Then
MsgBox ("Boa Tarde "+Wuser+", você acaba de ingressar na rede corporativa, por favor respeite as políticas de segurança e bom trabalho!")
Else
MsgBox ("Boa Noite "+wuser+", você acaba de ingressar na rede corporativa, por favor respeite as políticas de segurança e bom trabalho!")
End If

Wscript.Quit