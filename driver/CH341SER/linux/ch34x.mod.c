#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x732e219d, "module_layout" },
	{ 0x63d7caf0, "usb_serial_generic_tiocmiwait" },
	{ 0x52669ebe, "usb_serial_deregister_drivers" },
	{ 0x29212b86, "usb_serial_register_drivers" },
	{ 0xdb629fcc, "usb_serial_generic_resume" },
	{ 0x1aa1878e, "usb_serial_generic_open" },
	{ 0x19523f7c, "kmem_cache_alloc_trace" },
	{ 0xee6b6e86, "kmalloc_caches" },
	{ 0x30e74134, "tty_termios_copy_hw" },
	{ 0x409873e3, "tty_termios_baud_rate" },
	{ 0x6c257ac0, "tty_termios_hw_change" },
	{ 0xc2eb5c33, "usb_kill_urb" },
	{ 0xef71d84b, "usb_serial_generic_close" },
	{ 0x37a0cba, "kfree" },
	{  0xa9419, "usb_control_msg" },
	{ 0x9f026f68, "tty_kref_put" },
	{ 0x97ad6c7c, "usb_serial_handle_dcd_change" },
	{ 0x153c740a, "tty_port_tty_get" },
	{ 0x2acd040f, "dev_err" },
	{ 0x3c92488, "usb_submit_urb" },
	{ 0x3eeb2322, "__wake_up" },
	{ 0x9e413170, "__dynamic_dev_dbg" },
	{ 0x3812050a, "_raw_spin_unlock_irqrestore" },
	{ 0x51760917, "_raw_spin_lock_irqsave" },
	{ 0xbdfb6dbb, "__fentry__" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=usbserial,usbcore";

MODULE_ALIAS("usb:v4348p5523d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v1A86p7523d*dc*dsc*dp*ic*isc*ip*in*");
MODULE_ALIAS("usb:v1A86p5523d*dc*dsc*dp*ic*isc*ip*in*");

MODULE_INFO(srcversion, "43D0AA4C62168385556E2FA");
