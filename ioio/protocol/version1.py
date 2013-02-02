#!/usr/bin/env python
"""
see: firmware/app_layer_v1/protocol_defs.h
"""


def packet(char, *args):
    """
    args are bit ordered right to left so
        ('a', 1), ('b', 3) = bbba
    set arg[1] = 0 for variable length arguments
    """
    bitcount = 0
    for arg in args:
        if len(arg) == 2:
            k, n = arg
            t = None
        elif len(arg) == 3:
            k, n, t = arg
        else:
            raise ValueError('Invalid packet arg: %r, %s, ' \
                'must be len == 2 or 3' % (char, arg)
	if not isinstance(k, str):
            raise ValueError('arg[0] must be a string: %r, %s' \
                % (char, arg))
        if (k != '') and (not :
            if 
        if not(len(arg) > 1 and isinstance(arg[0], str) and
                isinstance(arg[1], int, str)) and arg[1] >= 0):
            raise ValueError('Invalid packet args: %r, %s' % (char, args))
        if len(arg) == 2 and (not arg[0] == ''):
            raise ValueError('Packet arg missing type: %r, %s' % (char, arg))
        bitcount += arg[1]
    if not ((bitcount == 0) or (bitcount % 8 == 0)):
        raise ValueError('Invalid bitcount[%s] for packet: %r, %s' %
                (bitcount, char, args))
    nbytes = int(bitcount / 8)
    return dict(char=char, args=args, nbytes=nbytes)


commands = {
    'hard_reset': packet('\x00',
        ('magic', 32, 'c')),
    'soft_reset': packet('\x01'),
    'check_interface': packet('\x02',
        ('interface', 64, 'c')),
    'set_pin_digital_out': packet('\x03',
        ('open_drain', 1, 'b'),
        ('value', 1, 'b'),
        ('pin', 6, 'i')),
    'set_digital_out_level': packet('\x04',
        ('value', 1, 'b'),
        ('', 1),
        ('pin', 6, 'i')),
    'set_pin_digital_in': packet('\x05',
        ('pull', 2, 'i'),
        ('pin', 6, 'i')),
    'set_change_notify': packet('\x06',
        ('cn', 1, 'b'),
        ('', 1),
        ('pin', 6, 'i')),
    'register_periodic_digital_sampling': packet('\x07',
        ('pin', 6, 'i'),
        ('', 2),
        ('freq_scale', 8, 'i')),
    'set_pin_pwm': packet('\x08',
        ('pin', 6, 'i'),
        ('', 2),
        ('pwm_num', 4, 'i'),
        ('', 3),
        ('enable', 1, 'b')),
    'set_pwm_duty_cycle': packet('\x09',
        ('fraction', 2, 'i'),
        ('pwm_num', 4, 'i'),
        ('', 2),
        ('dc', 16, 'i')),
    'set_pwm_period': packet('\x0A',
        ('scale_l', 1, 'i'),
        ('pwm_num', 4, 'i'),
        ('', 2),
        ('scale_h', 1, 'i'),
        ('period', 16, 'i')),
    'set_pin_analog_in': packet('\x0B',
        ('pin', 8, 'i')),
    'set_analog_in_sampling': packet('\x0C',
        ('pin', 6, 'i'),
        ('', 1),
        ('enable', 1, 'b')),
    'uart_config': packet('\x0D',
        ('parity', 2, 'i'),
        ('two_stop_bits', 1, 'b'),
        ('speed4x', 1, 'b'),
        ('', 2),
        ('uart_num', 2, 'i'),
        ('rate', 16, 'i')),
    'uart_data': packet('\x0E',
        ('size', 6, 'i'),
        ('uart_num', 2, 'i'),
        ('data', 'size', 'c')),
    'set_pin_uart': packet('\x0F',
        ('pin', 6, 'i'),
        ('', 2),
        ('uart_num', 2, 'i'),
        ('', 4),
        ('dir', 1, 'i'),
        ('enable', 1, 'i')),
    'spi_configure_master': packet('\x10',
        ('div', 3, 'i'),
        ('scale', 2, 'i'),
        ('spi_num', 2, 'i'),
        ('', 1),
        ('clk_pol', 1, 'b'),
        ('clk_edge', 1, 'b'),
        ('smp_end', 1, 'b'),
        ('', 5)),
    'spi_master_request': packet('\x11',
        ('ss_pin', 6, 'i'),
        ('spi_num', 2, 'i'),
        ('total_size', 6, 'i'),
        ('res_size_neq_total', 1, 'b'),
        ('data_size_neq_total', 1, 'b'),
        ('data_size', 8, 'i'),
        ('data', 'data_size', 'c')),
    'set_pin_spi': packet('\x12',
        ('pin', 6, 'i'),
        ('', 2),
        ('spi_num', 2, 'i'),
        ('mode', 2, 'i'),
        ('enable', 1, 'b'),
        ('', 3)),
    'i2c_configure_master': packet('\x13',
        ('i2c_num', 2, 'i'),
        ('', 3),
        ('rate', 2, 'i'),
        ('smbus_levels', 1, 'b')),
    'i2c_write_read': packet('\x14',
        ('i2c_num', 2, 'i'),
        ('', 3),
        ('ten_bit_addr', 1, 'b'),
        ('addr_msb', 2, 'i'),
        ('addr_lsb', 8, 'i'),
        ('write_size', 8, 'i'),
        ('read_size', 8, 'i'),
        ('data', 'write_size', 'c')),
    #'\x15': ''
    'icsp_six': packet('\x16',
        ('inst', 24, 'c')),
    'icsp_regout': packet('\x17'),
    'icsp_prog_enter': packet('\x18'),
    'icsp_prog_exit': packet('\x19'),
    # FIXME per the protocol only enable:1 is defined, i'm guessing the '':7
    'icsp_config': packet('\x1A',
        ('enable', 1, 'b'),
        ('', 7)),
    'incap_config': packet('\x1B',
        ('incap_num', 4, 'i'),
        ('', 4),
        ('clock', 2, 'i'),
        ('', 1),
        ('mode', 3, 'i'),
        ('', 1),
        ('double_prec', 1, 'b')),
    'set_pin_incap': packet('\x1C',
        ('pin', 6, 'i'),
        ('', 2),
        ('incap_num', 4, 'i'),
        ('', 3),
        ('enable', 1, 'b')),
    'soft_close': packet('\x1D'),
}

responses = {
    'establish_connection': packet('\x00',
        ('magic', 32, 'c'),
        ('hardware_version', 64, 'c'),
        ('board_version', 64, 'c'),
        ('firmware_version', 64, 'c')),
    #'\x01': ''
    'check_interface_response': packet('\x02',
        ('supported', 1, 'b'),
        ('', 7)),
    #'\x03': ''
    'report_digital_in_status': packet('\x04',
        ('level', 1, 'b'),
        ('', 1),
        ('pin', 6, 'i')),
    'report_periodic_digital_in_status': packet('\x05',
        ('size', 8, 'i')),
    #'\x06': ''
    #'\x07': ''
    #'\x08': ''
    #'\x09': ''
    #'\x0A': ''
    'report_analog_in_status': packet('\x0B'),
    'report_analog_in_format': packet('\x0C',
        ('num_pins', 8, 'i')),
    'uart_status': packet('\x0D',
        ('uart_num', 2, 'i'),
        ('', 5),
        ('enabled', 1, 'b')),
    'uart_data': packet('\x0E',
        ('size', 6, 'i'),
        ('uart_num', 2, 'i'),
        ('data', 'size', 'c')),
    # NOTE bytes_to_add = N of additional bytes to read
    'uart_report_tx_status': packet('\x0F',
        ('uart_num', 2, 'i'),
        ('bytes_to_add', 14, 'i')),
    'spi_status': packet('\x10',
        ('spi_num', 2, 'i'),
        ('', 5),
        ('enabled', 1, 'b')),
    'spi_data': packet('\x11',
        ('size', 6, 'i'),
        ('spi_num', 2, 'i'),
        ('ss_pin', 6, 'i'),
        ('', 2),
        ('data', 'size', 'c')),
    # NOTE bytes_to_add = N of additional bytes to read
    'spi_report_tx_status': packet('\x12',
        ('spi_num', 2, 'i'),
        ('bytes_to_add', 14, 'i')),
    'i2c_status': packet('\x13',
        ('i2c_num', 2, 'i'),
        ('', 5),
        ('enabled', 1, 'b')),
    'i2c_result': packet('\x14',
        ('i2c_num', 2, 'i'),
        ('', 6),
        ('size', 8, 'i')),
    # NOTE bytes_to_add = N of additional bytes to read
    'i2c_report_tx_status': packet('\x15',
        ('i2c_num', 2, 'i'),
        ('bytes_to_add', 14, 'i')),
    # NOTE bytes_to_add = N of additional bytes to read
    'icsp_report_rx_status': packet('\x16',
        ('bytes_to_add', 16, 'i')),
    'icsp_result': packet('\x17',
        ('reg', 16, 'c')),
    #'\x18': ''
    #'\x19': ''
    #'\x1A': ''
    'incap_status': packet('\x1B',
        ('incap_num', 4, 'i'),
        ('', 3),
        ('enabled', 1, 'b')),
    'incap_report': packet('\x1C',
        ('incap_num', 4, 'i'),
        ('', 2),
        ('size', 2, 'i')),
    'soft_close': packet('\x1D'),
}


class Version1Parser(object):
    pass
