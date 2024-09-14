import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import cover
from esphome.components import uart
from esphome.const import CONF_ID,CONF_ADDRESS

DEPENDENCIES = ["uart"]

nice_cover_ns = cg.esphome_ns.namespace("nice_cover")
NiceCover = nice_cover_ns.class_("NiceCover", cover.Cover, cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = cover.COVER_SCHEMA.extend(
    {cv.GenerateID(): cv.declare_id(NiceCover),
     cv.Optional(CONF_USE_ADDRESS): cv.hex_uint16_t}
).extend(cv.COMPONENT_SCHEMA).extend(uart.UART_DEVICE_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await cover.register_cover(var, config)
    await uart.register_uart_device(var, config)

    if CONF_ADDRESS in config:
        address = config[CONF_ADDRESS]
        cg.add(var.set_to_address(address))
