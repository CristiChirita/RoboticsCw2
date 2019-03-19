
"use strict";

let RegisterGui = require('./RegisterGui.js')
let AddCO2Source = require('./AddCO2Source.js')
let MoveRobot = require('./MoveRobot.js')
let DeleteRfidTag = require('./DeleteRfidTag.js')
let AddSoundSource = require('./AddSoundSource.js')
let DeleteCO2Source = require('./DeleteCO2Source.js')
let LoadMap = require('./LoadMap.js')
let AddThermalSource = require('./AddThermalSource.js')
let LoadExternalMap = require('./LoadExternalMap.js')
let DeleteThermalSource = require('./DeleteThermalSource.js')
let DeleteSoundSource = require('./DeleteSoundSource.js')
let AddRfidTag = require('./AddRfidTag.js')

module.exports = {
  RegisterGui: RegisterGui,
  AddCO2Source: AddCO2Source,
  MoveRobot: MoveRobot,
  DeleteRfidTag: DeleteRfidTag,
  AddSoundSource: AddSoundSource,
  DeleteCO2Source: DeleteCO2Source,
  LoadMap: LoadMap,
  AddThermalSource: AddThermalSource,
  LoadExternalMap: LoadExternalMap,
  DeleteThermalSource: DeleteThermalSource,
  DeleteSoundSource: DeleteSoundSource,
  AddRfidTag: AddRfidTag,
};
